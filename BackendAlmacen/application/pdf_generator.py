from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
from django.conf import settings
from datetime import datetime

def generate_deliverie_pdf(deliverie):
    # Nombre del archivo
    file_name = f"Resguardo_{deliverie.id_deliverie}.pdf"
    file_path = os.path.join(settings.MEDIA_ROOT, 'documents', 'deliveries', file_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4
    date_generation = deliverie.datetime.strftime("%d/%m/%Y")

    # Título
    c.setFont("RESGUARDO", 16)
    c.drawString(50, height - 50, "CARTA RESPONSIVA RESGUARDO DE EQUIPO ")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 180, f"Fresnillo, Zacatecas a {date_generation}")


    # Datos del modelo
    c.drawString(50, height - 100, f"")

    # Espacio para firma
    c.drawString(50, height - 240, "Firma de entrega: ______________________")
    c.drawString(50, height - 270, "Firma de recepción: ____________________")

    c.showPage()
    c.save()

    # Guardamos la ruta relativa al modelo
    deliverie.document = f'documents/deliveries/{file_name}'
    deliverie.save()
    return deliverie.document