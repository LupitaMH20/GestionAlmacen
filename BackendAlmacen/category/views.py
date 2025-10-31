from rest_framework import viewsets
from .models import Category
from .serializer import CategorySerializers

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    lookup_field = 'id_Category'

    def get_queryset(self):
        show_inactive = self.request.query_params.get('inactive', 'false').lower() == 'true'
        if show_inactive:
            return Category.objects.filter(active=False)
        return Category.objects.filter(active=True)