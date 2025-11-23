from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import *
from django.db import transaction
from rest_framework import serializers

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all().order_by('-request_datetime')
    serializer_class = RequestSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializer.ValidationError as e:
            print("Error en la validación:", serializer.errors) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user=serializer.validated_data.get('user')
        if user.position != 'applicant':
            return Response(
                {"error": "Solo los solicitantes pueden crear preSolicitudes"},
                status=status.HTTP_403_FORBIDDEN
            )
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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
        
        # if authorizer.company != linked_request.requestingCompany:
        #     return Response(
        #         {"error": "No perteneces a la empresa de esta solicitud."},
        #         status=status.HTTP_403_FORBIDDEN
        #     )
        
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
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        linked_request = serializer.instance.requestActions.acceptance.request
        linked_request.status = 'supply'
        linked_request.save(update_fields=['status'])

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ReturnExchangeViewSet(viewsets.ModelViewSet):
    queryset = ReturnExchange.objects.all().order_by('-returnE_datetime')
    serializer_class = ReturnExchangeSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializer.ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        linked_request = serializer.instance.supply.requestActions.acceptance.request
        linked_request.status = 'returnExchange'
        linked_request.save(update_fields=['status'])

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# Se puede hacer manual mente pero ya esta que se haga automaticamente ya es innecesaria
# def archive_request(request, request_id):
#     try:
#         req = Request.objects.get(id_Request=request_id)
#         if req.status not in ['supply']:
#             return Response({"error": "Debe de estar terminada para que se pueda archivar"}, status=status.HTTP_400_BAD_REQUEST)
#         req.status = 'archived'
#         req.save(update_fields=['status'])
#         return Response({"mensaje": "Archivada"}, status=status.HTTP_200_OK)
#     except Request.DoesNotExist:
#         return Response({"error": "Solicitud no econtrada."}, status=status.HTTP_404_NOT_FOUND)