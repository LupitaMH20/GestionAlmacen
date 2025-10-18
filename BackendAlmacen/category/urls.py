from rest_framework import routers
from .views import CategoryViewSets

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSets, basename='category')

urlpatterns = router.urls