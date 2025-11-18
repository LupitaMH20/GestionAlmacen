from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router =DefaultRouter()
router.register(r'request', RequestViewSet, basename='request')
router.register(r'acceptance', AcceptanceViewSet, basename='acceptance')
router.register(r'requestActions', RequestActionsViewSet, basename='requestActions')
router.register(r'supply', SupplyViewSet, basename='supply')
# router.register(r'returnExchange', ReturnExchangeViewSet, basename='returnExchange')

urlpatterns = router.urls

urlpatterns += [
    path('request/<int:request_id>/finish/', finish_request, name='finish_request'),
    path('request/<int:request_id>/archive/', archive_request, name='archive_request'),
]