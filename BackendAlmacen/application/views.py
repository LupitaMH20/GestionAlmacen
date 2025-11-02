from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from django.db import transaction
from rest_framework import serializers

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all().order_by('-request_datetime')
    serializer_class = RequestSerializer

class AcceptanceViewSet(viewsets.ModelViewSet):
    queryset = Acceptance.objects.all().order_by('-acceptance_datetime')
    serializer_class = AcceptanceSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        linked_request = serializer.instance.request
        linked_request.status = 'request'
        linked_request.save(update_fields=['status'])

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class RequestActionsViewSet(viewsets.ModelViewSet):
    queryset = RequestActions.objects.all().order_by('-requestactions_datetime')
    serializer_class = RequestActionsSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        linked_request = serializer.instance.acceptance.request
        action_taken = serializer.instance.action

        if action_taken == 'authorize':
            linked_request.status = 'authorized'
        elif action_taken == 'decline':
            linked_request.status = 'declined'
        linked_request.save(update_fields=['status'])

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
    
@api_view(['POST'])
def finish_request(request, request_id):
    try:
        req = Request.objects.get(id_Request=request_id)
        if req.status != 'supply':
            return Response({"error": "Debe de entregarse para que se pueda terminar"}, status=status.HTTP_400_BAD_REQUEST)
        req.status = 'finished'
        req.save(update_fields=['status'])
        return Response({"mensaje": "Terminada"}, status=status.HTTP_200_OK)
    except Request.DoesNotExist:
        return Response({"error": "Solicitud no econtrada."}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def archive_request(request, request_id):
    try:
        req = Request.objects.get(id_Request=request_id)
        if req.status not in ['finished']:
            return Response({"error": "Debe de estar terminada para que se pueda archivar"}, status=status.HTTP_400_BAD_REQUEST)
        req.status = 'archived'
        req.save(update_fields=['status'])
        return Response({"mensaje": "Archivada"}, status=status.HTTP_200_OK)
    except Request.DoesNotExist:
        return Response({"error": "Solicitud no econtrada."}, status=status.HTTP_404_NOT_FOUND)