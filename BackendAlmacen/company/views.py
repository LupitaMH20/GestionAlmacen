from rest_framework import viewsets
from .models import Companies
from .serializers import CompanySerializer

class CompanyViewSets(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    lookup_field = 'id_Company'

    def get_queryset(self):
        show_inactive =self.request.query_params.get('inactive', 'false').lower() =='true'
        if show_inactive:
            return Companies.objects.filter(active=False)
        return Companies.objects.filter(active=True)