from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from . import views

router =DefaultRouter()
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from . import views

router =DefaultRouter()
router.register(r'request', RequestViewSet, basename='request')
router.register(r'acceptance', AcceptanceViewSet, basename='acceptance')
router.register(r'requestActions', RequestActionsViewSet, basename='requestActions')
router.register(r'supply', SupplyViewSet, basename='supply')
# router.register(r'returnExchange', ReturnExchangeViewSet, basename='returnExchange')

urlpatterns = [
    # ... tus otras URLs
    path('request/<int:request_id>/archive/', archive_request, name='archive_request'),
    path('request/<int:request_id>/checkout-pdf/', 
        views.download_equipment_checkout_pdf, 
        name='download_checkout_pdf'),
    path('request/<int:request_id>/quote-pdf/', 
        views.download_quote_pdf, 
        name='download_quote_pdf'),
    path('request/bulk-quote-pdf/', 
        views.download_bulk_quote_pdf, 
        name='download_bulk_quote_pdf'),
] + router.urls