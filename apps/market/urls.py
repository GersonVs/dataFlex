from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, CreateOrderAPIView

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
# router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls)),

    path('create_order', CreateOrderAPIView.as_view())
]
