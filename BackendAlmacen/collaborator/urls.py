from rest_framework.routers import DefaultRouter
from .views import CollaboratorViewSets

router = DefaultRouter()
router.register(r'collaborator', CollaboratorViewSets, basename='collaborator')

urlpatterns = router.urls