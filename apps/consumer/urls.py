from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, ClientAddressViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'client-addresses', ClientAddressViewSet, basename='client-addresses')

urlpatterns = [
    path('', include(router.urls)),
]