from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import *
from django.db import transaction
from rest_framework import serializers
from .pdf.pdf_generator import ReportPDFGenerator, PDFGenerator
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404
from article.models import Articles
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all().order_by('-request_datetime')
    serializer_class = RequestSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            print("Error en la validación:", serializer.errors) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user=serializer.validated_data.get('user')
        if user.position != 'applicant':
            return Response(
                {"error": "Solo los solicitantes pueden crear preSolicitudes"},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Validar si el artículo existe y está activo
        article_id = request.data.get('article')
        if article_id:
            try:
                article_obj = Articles.objects.get(id_mainarticle=article_id)
                if not article_obj.active:
                    return Response(
                        {"error": f"El artículo '{article_obj.name}' está desactivado. No se pueden crear solicitudes para artículos inactivos."},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            except Articles.DoesNotExist:
                # Si el artículo no existe, permitimos la solicitud (comportamiento actual para texto libre)
                pass
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['post'])
    def decline_prerequest(self, request, pk=None):
        """Rechaza una pre-solicitud"""
        req = self.get_object()
        
        if req.status != 'prerequest':
            return Response(
                {"error": "Solo se pueden rechazar pre-solicitudes en estado 'prerequest'"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        reason = request.data.get('reason')
        if not reason:
            return Response(
                {"error": "Se requiere un motivo de rechazo"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        req.status = 'declined'
        req.rejection_reason = reason
        req.save()
        
        return Response({"status": "Pre-solicitud rechazada"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def regenerate_request(self, request, pk=None):
        """Regenera una solicitud rechazada a pre-solicitud"""
        req = self.get_object()
        
        if req.status != 'declined':
            return Response(
                {"error": "Solo se pueden regenerar solicitudes en estado 'declined'"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        req.status = 'prerequest'
        req.rejection_reason = None # Limpiar motivo al regenerar
        req.save()
        
        return Response({"status": "Solicitud regenerada a pre-solicitud"}, status=status.HTTP_200_OK)

class AcceptanceViewSet(viewsets.ModelViewSet):
    queryset = Acceptance.objects.all().order_by('-acceptance_datetime')
    serializer_class = AcceptanceSerializer
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data
        pre_request = validated_data.get('request')
        acceptor = request.user

        if acceptor.position in ['applicant', 'deliberystaff']:
            return Response(
                {"error": "No tienes permisos para aceptar solicitudes."},
                status=status.HTTP_403_FORBIDDEN
            )

        article_id_mainarticle = pre_request.article
        requested_amount = pre_request.amount

        try:
            article_to_supply = Articles.objects.get(id_mainarticle__iexact=article_id_mainarticle)
        except Articles.DoesNotExist:
            return Response(
                {"error": f"Artículo no registrado en el sistema: '{article_id_mainarticle}'. No se puede aceptar."},
                status=status.HTTP_404_NOT_FOUND 
            )
        

        # Lógica de reintento: Si la solicitud ya fue aceptada (probablemente rechazada y regenerada),
        # limpiamos la aceptación previa "stale" para permitir el nuevo flujo.
        if hasattr(pre_request, 'acceptance'):
            print(f"Limpiando aceptación previa para solicitud {pre_request.id_Request}")
            pre_request.acceptance.delete()

        # Validar si el artículo está activo
        if not article_to_supply.active:
            return Response(
                {"error": f"El artículo '{article_to_supply.name}' está desactivado. No se puede aceptar la solicitud."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if article_to_supply.stock < requested_amount:
            return Response(
                {"error": f"Stock insuficiente. Solicitados: {requested_amount}, Disponibles: {article_to_supply.stock}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        article_to_supply.stock -= requested_amount
        article_to_supply.save()
        pre_request.status = 'request'
        pre_request.save()

        acceptance_instance = serializer.save(user=acceptor, article=article_to_supply)
        
        return Response(
            {"success": "Solicitud aceptada y stock actualizado.", "data": serializer.data},
            status=status.HTTP_201_CREATED
        )

class RequestActionsViewSet(viewsets.ModelViewSet):
    queryset = RequestActions.objects.all().order_by('-requestactions_datetime')
    serializer_class = RequestActionsSerializer
    permission_classes =[IsAuthenticated]

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        acceptance_to_action = serializer.validated_data.get('acceptance')
        action_taken = serializer.validated_data.get('action')
        authorizer = request.user
        comment = serializer.validated_data.get('comment')

        linked_request = acceptance_to_action.request
        original_requester = linked_request.user

        if authorizer.id_user == original_requester.id_user:
            return Response({"error": "No puedes autorizar o rechazar tus propias solicitudes."}, status=status.HTTP_403_FORBIDDEN)
        
        if authorizer.position in ['applicant', 'deliberystaff']:
            return Response(
                {"error": "No tienes permisos para authorizar o rechazar."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        existing_action = None
        if hasattr(acceptance_to_action, 'requestactions'):
            existing_action = acceptance_to_action.requestactions
        
        if existing_action:
            existing_action.action = action_taken
            existing_action.comment = comment
            existing_action.user = authorizer
            existing_action.save()
            
            linked_request.status = action_taken
            linked_request.save(update_fields=['status'])
            
            response_serializer = self.get_serializer(existing_action)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        
        else:
            linked_request.status = action_taken
            linked_request.save(update_fields=['status'])
            serializer.save(user=authorizer)
            
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all().order_by('-supply_datetime')
    serializer_class = SupplySerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            print("ERRORES SUPPLY:", serializer.errors)
            return Response({"error": str(e), "detail": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        linked_request = serializer.instance.requestActions.acceptance.request
        linked_request.status = 'supply'
        linked_request.save(update_fields=['status'])

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# PDF Views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def download_equipment_checkout_pdf(request, request_id):
    """Descarga el PDF de resguardo de equipo"""
    
    checkout_request = get_object_or_404(Request, id_Request=request_id)
    collaborator = checkout_request.collaborator
    
    try:
        article = Articles.objects.get(id_mainarticle=checkout_request.article)
    except Articles.DoesNotExist:
        class DummyArticle:
            name = checkout_request.article
            description = "Artículo no encontrado"
            id_mainarticle = checkout_request.article
        article = DummyArticle()

    company = checkout_request.requestingCompany
    
    pdf = ReportPDFGenerator.generate_equipment_checkout_pdf(
        checkout_request,
        collaborator,
        article,
        company
    )
    
    if pdf:
        return FileResponse(
            pdf,
            as_attachment=True,
            filename=f"Resguardo_Equipo_{checkout_request.id_Request}.pdf",
            content_type="application/pdf"
        )
    else:
        return HttpResponse("Error al generar el PDF", status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def download_quote_pdf(request, request_id):
    """Descarga el PDF de cotización individual"""
    
    quote_request = get_object_or_404(Request, id_Request=request_id)
    
    try:
        article = Articles.objects.get(id_mainarticle=quote_request.article)
    except Articles.DoesNotExist:
        class DummyArticle:
            name = quote_request.article
            description = "Artículo no encontrado"
            id_mainarticle = quote_request.article
            price = 0
        article = DummyArticle()

    pdf = PDFGenerator.generate_quote_pdf(quote_request, article)
    
    if pdf:
        return FileResponse(
            pdf,
            as_attachment=True,
            filename=f"Cotizacion_{quote_request.id_Request}.pdf",
            content_type="application/pdf"
        )
    else:
        return HttpResponse("Error al generar el PDF de cotización", status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def download_bulk_quote_pdf(request):
    """Descarga un PDF con múltiples solicitudes (reporte)"""
    
    request_ids = request.data.get('request_ids', [])
    
    if not request_ids:
        return Response(
            {"error": "No se proporcionaron IDs de solicitud"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Obtener todas las solicitudes
    requests_objs = Request.objects.filter(
        id_Request__in=request_ids
    ).order_by('-request_datetime')
    
    if not requests_objs.exists():
        return Response(
            {"error": "No se encontraron solicitudes"}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    # Obtener artículos para cada solicitud
    articles_map = {}
    for req in requests_objs:
        try:
            article = Articles.objects.get(id_mainarticle=req.article)
        except Articles.DoesNotExist:
            # Crear objeto dummy si no existe
            class DummyArticle:
                def __init__(self, name, article_id):
                    self.name = name
                    self.description = "Artículo no encontrado"
                    self.id_mainarticle = article_id
                    self.price = 0
            
            article = DummyArticle(req.article, req.article)
        
        articles_map[req.id_Request] = article
    
    # Generar PDF
    pdf = PDFGenerator.generate_bulk_quote_pdf(list(requests_objs), articles_map)
    
    if pdf:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        return FileResponse(
            pdf,
            as_attachment=True,
            filename=f"Reporte_Solicitudes_{timestamp}.pdf",
            content_type="application/pdf"
        )
    else:
        return HttpResponse("Error al generar el PDF de reporte", status=400)

@api_view(['POST'])
def archive_request(request, request_id):
    """Archiva una solicitud manualmente"""
    try:
        req = Request.objects.get(id_Request=request_id)
        if req.status not in ['supply']:
            return Response(
                {"error": "Debe de estar terminada para que se pueda archivar"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Validar pago para Herramientas
        if req.type == 'Tool':
            try:
                # Navegar a través de las relaciones: Request -> Acceptance -> RequestActions -> Supply
                supply = req.acceptance.requestactions.supply
                if supply.payment_status != 'paid':
                    return Response(
                        {"error": "Las solicitudes de Herramienta deben estar pagadas para poder archivarse."}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
            except Exception as e:
                # Si hay error en la navegación de relaciones (datos corruptos), loguear y opcionalmente bloquear
                print(f"Error verificando pago para request {req.id_Request}: {str(e)}")
                # Decisión: Si no se encuentra el suministro o hay error, bloqueamos por seguridad
                return Response(
                    {"error": "No se pudo verificar el estado de pago. Contacte a soporte."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        req.status = 'archived'
        req.save(update_fields=['status'])
        return Response({"mensaje": "Archivada"}, status=status.HTTP_200_OK)
    except Request.DoesNotExist:
        return Response(
            {"error": "Solicitud no encontrada."}, 
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['GET'])
@permission_classes([])  # No se necesita autenticación
def health_check(request):
    """
    Verificación de estado simple para Docker.
    """
    return Response({"status": "ok", "message": "Backend is healthy."}, status=status.HTTP_200_OK)

@api_view(['POST'])
def upload_pdf_view(request):
    """
    Endpoint para subir PDFs a Supabase Storage.
    """
    from .supabase_storage import supabase_storage
    if 'file' not in request.FILES:
        return Response(
            {"error": "No se proporcionó ningún archivo"},
            status=status.HTTP_400_BAD_REQUEST
        )

    pdf_file = request.FILES['file']

    # Validar que sea PDF
    if not pdf_file.name.endswith('.pdf'):
        return Response(
            {"error": "Solo se permiten archivos PDF"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Generar ruta única
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"solicitudes/{timestamp}_{pdf_file.name}"

    # Subir a Supabase
    result = supabase_storage.upload_pdf(pdf_file, path)

    if result["success"]:
        return Response(result, status=status.HTTP_201_CREATED)
    else:
        return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)