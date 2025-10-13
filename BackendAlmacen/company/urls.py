from rest_framework.routers import DefaultRouter
from .views import CompanyViewSets

router = DefaultRouter()
router.register(r'companies', CompanyViewSets, basename='company')

urlpatterns = router.urls