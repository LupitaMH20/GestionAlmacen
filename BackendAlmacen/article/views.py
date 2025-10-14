from rest_framework import viewsets
from .models import Articles
from .serializer import ArticleSerializers

class ArticlesViewSets(viewsets.ModelViewSet):
    serializer_class = ArticleSerializers
    lookup_field ='id_mainarticle'

    def get_queryset(self):
        show_inactive = self.request.query_params.get('inactive', 'false').lower() == 'true'
        if show_inactive:
            return Articles.objects.filter(active=False)
        return Articles.objects.filter(active=True)