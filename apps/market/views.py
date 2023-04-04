from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer, OrderSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreateOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]


    @swagger_auto_schema(
        operation_description="Cria um novo pedido",
        request_body=OrderSerializer,
        responses={
            201: OrderSerializer(),
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            500: "Internal Server Error"
        },
        tags=['market']
    )
    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
