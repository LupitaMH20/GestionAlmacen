from rest_framework.routers import DefaultRouter
from .views import UserViewSets

router = DefaultRouter()
router.register(r'users', UserViewSets, basename='user')

urlpatterns = router.urls