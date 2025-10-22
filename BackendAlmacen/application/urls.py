from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router =DefaultRouter()
router.register(r'prerequest', views.PreRequestViewSet, basename='prerequest')
router.register(r'request', views.RequestViewSet, basename='request')
router.register(r'authorize', views.AuthorizeViewSet, basename='authorize')
router.register(r'decline', views.DeclineViewSet, basename='decline')

urlpatterns = router.urls