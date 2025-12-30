# En users/views.py

from rest_framework.decorators import action
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Users
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings


class UserViewSets(viewsets.ModelViewSet): 
    serializer_class = UserSerializer
    lookup_field = 'id_user'

    def get_queryset(self):
        queryset = Users.objects.all()
        position = self.request.query_params.get('position', None)
        if position:
            queryset = queryset.filter(position=position)
        show_inactive = self.request.query_params.get('inactive', 'false').lower() == 'true'
        if show_inactive:
            queryset = queryset.filter(active=False)
        else:
            queryset = queryset.filter(active=True)
        return queryset
    
    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        name = request.data.get('name')
        password = request.data.get('password')
        try:
            user = Users.objects.get(name=name)
            if not check_password(password, user.password):
                raise Users.DoesNotExist
            if not user.active:
                return Response({'error': 'Usuario inactivo.'}, status=status.HTTP_403_FORBIDDEN)

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            serializer = UserSerializer(user)

            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': access_token
            }, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response({'error': 'No existe el usuario'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)