from rest_framework import viewsets
from .models import Users
from .serializers import UserSerializer

class UserViewSets(viewsets.ModelViewSet): 
    serializer_class = UserSerializer
    lookup_field = 'id_user'

    def get_queryset(self):
        show_inactive = self.request.query_params.get('inactive', 'false').lower() == 'true'
        if show_inactive:
            return Users.objects.filter(active=False)
        return Users.objects.filter(active=True)