from rest_framework.routers import DefaultRouter
from .views import ArticlesViewSets

router = DefaultRouter()
router.register(r'article', ArticlesViewSets, basename='article')

urlpatterns = router.urls