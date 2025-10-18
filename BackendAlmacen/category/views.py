from rest_framework import viewsets
from .models import Category
from .serializer import CategorySerializers

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    lookup_field = 'id_Category'