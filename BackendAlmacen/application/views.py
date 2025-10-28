from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

class PreRequestViewSet(viewsets.ModelViewSet):
    queryset = PreRequest.objects.all().order_by('-requested_datetime')
    serializer_class = PreRequestSerializer

# En views.py
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all().order_by('-request_datetime')
    serializer_class = RequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            print("Errores de validación:", serializer.errors)
            raise e
        self.perform_create(serializer)
        prerequest = serializer.instance.prerequest
        prerequest.status = 'request'
        prerequest.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class AuthorizeViewSet(viewsets.ModelViewSet):
    queryset = Authorize.objects.all().order_by('-authorized_datetime')
    serializer_class = AuthorizeSerializer

class DeclineViewSet(viewsets.ModelViewSet):
    queryset = Decline.objects.all().order_by('-datetime')
    serializer_class = DeclineSerializer

@api_view(['POST'])
def advance_request(request, id_Request):
    req = Request.objects.get(id_Request=id_Request)
    action = request.data.get('action')

    if action == 'authorize':
        serializer = AuthorizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request=req)
            req.status = 'authorized'
    elif action == 'decline':
        serializer = DeclineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request=req)
            req.status = 'declined'
    elif action == 'deliver':
        serializer = DeliverieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request=req)
            req.status = 'delivered'
    elif action == 'return':
        serializer = ReturnExchangeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(deliverie=req.deliverie)
            req.status = 'returned'

    req.save()
    return Response({'status': 'success', 'new_state': req.status})