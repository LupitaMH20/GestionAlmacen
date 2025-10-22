from rest_framework import viewsets
from .models import Users
from .serializers import UserSerializer

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