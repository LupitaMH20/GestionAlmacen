from rest_framework import viewsets
from .models import Collaborators
from .serializer import Collaboratorserializers

class CollaboratorViewSets(viewsets.ModelViewSet):
    serializer_class = Collaboratorserializers
    lookup_field = 'id_Collaborator'

    def get_queryset(self):
        show_inactive = self.request.query_params.get('inactive', 'false').lower() == 'true'
        if show_inactive:
            return Collaborators.objects.filter(active=False)
        return Collaborators.objects.filter(active=True)