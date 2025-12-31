from io import BytesIO
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime

class PDFGenerator:
    @staticmethod
    def fmt_decimal(value) -> str:
        if value is None:
            return "0.00"

        if not isinstance(value, Decimal):
            try:
                value = Decimal(str(value))
            except (ValueError, TypeError):
                return "0.00"

        value = value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        return f"{value:,.2f}"

    @staticmethod
    def value_to_text(value):
        return f"{value} (Monto en texto pendiente)"

    @staticmethod
    def get_logo_url(company_name):
        """
        Retorna la URL del logo según el nombre de la empresa.
        Busca coincidencias parciales (case-insensitive) en el nombre.
        """
        if not company_name:
            # Logo por defecto si no hay empresa
            return "https://res.cloudinary.com/dxhjcaqpk/image/upload/v1760545192/JOM_q0pkvn.png"
        
        # Normalizar el nombre de la empresa para comparación
        company_lower = str(company_name).lower().strip()
        
        # Mapeo de empresas a logos (orden de prioridad)
        logos_map = {
            "printek": "https://res.cloudinary.com/dxhjcaqpk/image/upload/v1764646153/Printek_l2fhcv.png",
            "insumos": "https://res.cloudinary.com/dxhjcaqpk/image/upload/v1764646153/Logo-Insumos-Mineros-Soluciones-Integrales_ls5tjx.png",
            "naranja": "https://res.cloudinary.com/dxhjcaqpk/image/upload/v1764646153/Naranja-Store-Ferreterias_mppkih.png",
            "jom": "https://res.cloudinary.com/dxhjcaqpk/image/upload/v1760545192/JOM_q0pkvn.png",
        }
        
        # Buscar coincidencia exacta primero
        if company_lower in logos_map:
            print(f"✅ Logo encontrado (exacto): {company_name} -> {logos_map[company_lower]}")
            return logos_map[company_lower]
        
        # Buscar coincidencia parcial
        for key, logo_url in logos_map.items():
            if key in company_lower or company_lower in key:
                print(f"✅ Logo encontrado (parcial): {company_name} contiene '{key}' -> {logo_url}")
                return logo_url
        
        # Si no se encuentra, usar JOM por defecto
        print(f"⚠️ Logo no encontrado para '{company_name}', usando JOM por defecto")
        return logos_map["jom"]


    @staticmethod
    def generate_quote_pdf(request, article_obj):
        return PDFGenerator.generate_bulk_quote_pdf([request], [article_obj])

    @staticmethod
    def generate_bulk_quote_pdf(requests, articles_map):
        items = []
        grand_total = Decimal("0.00")
        
        first_req = requests[0] if requests else None
        
        if not first_req:
            return None

        company_name = first_req.requestingCompany.name
        company_address = first_req.requestingCompany.address
        
        same_company = all(
            r.requestingCompany.id_Company == first_req.requestingCompany.id_Company 
            for r in requests
        )
        
        if not same_company:
            company_name = "Varios Clientes"
            company_address = "---"

        for i, req in enumerate(requests):
            # Obtener artículo
            article_obj = None
            if isinstance(articles_map, dict):
                article_obj = articles_map.get(req.id_Request)
            elif isinstance(articles_map, list) and len(articles_map) > i:
                article_obj = articles_map[i]
            
            quantity = req.amount
            
            # Obtener precio
            price = Decimal("0.00")
            if article_obj and hasattr(article_obj, 'price'):
                try:
                    price = Decimal(str(article_obj.price))
                except:
                    price = Decimal("0.00")
            
            subtotal = price * Decimal(str(quantity))
            grand_total += subtotal
            
            # Mapear status
            status_map = {
                'archived': 'Archivado',
                'supply': 'Surtido',
                'finished': 'Finalizado',
                'declined': 'Rechazado',
                'request': 'Solicitado',
                'authorized': 'Autorizado',
                'prerequest': 'Pre-solicitud'
            }
            status_label = status_map.get(req.status, req.status)
            
            # Formatear fecha
            date_str = req.request_datetime.strftime("%d/%m/%Y") if req.request_datetime else "---"
            time_str = req.request_datetime.strftime("%H:%M") if req.request_datetime else ""

            # Tipo de solicitud - CORREGIDO
            type_map = {
                'Consumable': 'Consumible',
                'Tool': 'Herramienta',
                'PersonalConsumption': 'Consumo Personal'
            }
            req_type = type_map.get(req.type, req.type)

            items.append({
                "id": req.id_Request,
                "status": req.status,
                "status_label": status_label,
                "date": date_str,
                "time": time_str,
                "type": req_type,
                "article_name": getattr(article_obj, 'name', req.article),
                "article_id": req.article,
                "amount": quantity,
                "unit_price": PDFGenerator.fmt_decimal(price),
                "total": PDFGenerator.fmt_decimal(subtotal),
                "requester": f"{req.user.name} {getattr(req.user, 'last_name', '')}".strip(),
                "company": req.requestingCompany.name if req.requestingCompany else "---"
            })

        company_logo = PDFGenerator.get_logo_url(company_name if same_company else "JOM")
        
        context = {
            "title": "REPORTE DE SOLICITUDES",
            "company_info": {
                "logo_url": company_logo,
                "razon_social": company_name,
                "direccion": company_address,
            },
            "items": items,
            "grand_total": PDFGenerator.fmt_decimal(grand_total),
        }

        html_string = render_to_string("application/pdf/quote_pdf.html", context)
        pdf_file = BytesIO()
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)

        if pisa_status.err:
            return None

        pdf_file.seek(0)
        return pdf_file


class ReportPDFGenerator:
    """Generador de PDFs para reportes usando xhtml2pdf"""

    @staticmethod
    def _generate_pdf(template_name, context):
        """Método interno para generar PDF desde template HTML"""
        html = render_to_string(template_name, context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)

        if not pdf.err:
            result.seek(0)
            return result
        return None

    @staticmethod
    def generate_top_products_pdf(products, start_date, end_date):
        """Genera PDF de productos más cotizados"""
        context = {
            "products": products,
            "start_date": start_date.strftime("%d/%m/%Y"),
            "end_date": end_date.strftime("%d/%m/%Y"),
            "total_products": len(products),
            "logo_path": "https://res.cloudinary.com/dxhjcaqpk/image/upload/v1760545192/JOM_q0pkvn.png",
        }
        return ReportPDFGenerator._generate_pdf(
            "reports/pdf/top_products.html", context
        )

    @staticmethod
    def generate_customer_stats_pdf(stats, start_date, end_date):
        """Genera PDF de estadísticas por cliente"""
        context = {
            "stats": stats,
            "start_date": start_date.strftime("%d/%m/%Y"),
            "end_date": end_date.strftime("%d/%m/%Y"),
            "total_customers": len(stats),
            "logo_path": "https://res.cloudinary.com/dxhjcaqpk/image/upload/v1760545192/JOM_q0pkvn.png",
        }
        return ReportPDFGenerator._generate_pdf(
            "reports/pdf/customer_stats.html", context
        )

    @staticmethod
    def generate_global_stats_pdf(stats, start_date, end_date):
        """Genera PDF de estadísticas globales"""
        context = {
            "stats": stats,
            "start_date": start_date.strftime("%d/%m/%Y"),
            "end_date": end_date.strftime("%d/%m/%Y"),
            "logo_path": "https://res.cloudinary.com/dxhjcaqpk/image/upload/v1760545192/JOM_q0pkvn.png",
        }
        return ReportPDFGenerator._generate_pdf(
            "reports/pdf/global_stats.html", context
        )

    @staticmethod
    def generate_equipment_checkout_pdf(request, collaborator, article, company):
        """Genera PDF de entrega de equipo (Resguardo)"""
        
        # Datos por defecto
        if not hasattr(request, 'credential_number'):
            request.credential_number = "N/A"
        if not hasattr(request, 'serial_number'):
            request.serial_number = "N/A"
        if not hasattr(request, 'phone_number'):
            request.phone_number = "N/A"
        
        # Fecha en español
        months = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
            7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }
        
        date_obj = request.request_datetime
        if date_obj:
            formatted_date = f"{date_obj.day} de {months.get(date_obj.month, '')} de {date_obj.year}"
        else:
            now = datetime.now()
            formatted_date = f"{now.day} de {months.get(now.month, '')} de {now.year}"
            
        # Especificaciones del artículo
        if not hasattr(article, 'specs'):
            specs = []
            if article.description:
                parts = article.description.split(',')
                for part in parts:
                    if ':' in part:
                        key, value = part.split(':', 1)
                        specs.append({'key': key.strip(), 'value': value.strip()})
                    else:
                        specs.append({'key': 'Descripción', 'value': part.strip()})
            
            if not specs:
                specs.append({'key': 'Descripción', 'value': article.description or "Sin descripción"})
            
            article.specs = specs

        # Traducir posición
        position_map = {
            "applicant": "Solicitante",
            "deliberystaff": "Repartidor",
            "admin": "Administrador",
            "manager": "Gerente",
            "warehouse": "Almacenista"
        }
        
        collaborator_position_es = position_map.get(
            str(collaborator.position).lower(), 
            collaborator.position
        )

        logo_path = PDFGenerator.get_logo_url(company.name)

        context = {
            "request": request,
            "collaborator": collaborator,
            "collaborator_position": collaborator_position_es,
            "article": article,
            "company": company,
            "formatted_date": formatted_date,
            "logo_path": logo_path,
        }
        
        return ReportPDFGenerator._generate_pdf(
            "reports/pdf/equipment_checkout.html", context
        )