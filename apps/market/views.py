from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import OrderItem, Product, Order
from .serializers import ProductSerializer, OrderSerializer, DetailOrderItemSerializer, DetailOrderSerializer
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
        serializer.is_valid(raise_exception=True)
        
        # Cria o pedido
        order_data = serializer.validated_data
        order = Order.objects.create(
            client=order_data['client'],
            client_address=order_data['client_address']
        )

        # Cria os items do pedido
        items_data = order_data['items']
        
        total_value = 0
        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            total_item_value = product.price * quantity
            
            order_item = OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                total_value=total_item_value,
            )

            total_value += total_item_value

        # atualiza o valor total do pedido
        order.total_value = total_value
        order.save()

        return Response({
            'order_id': order.id,
            'message': 'Pedido criado com sucesso!'
        }, status=status.HTTP_201_CREATED)


class OrderDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Obtém os detalhes de um pedido",
        responses={
            201: OrderSerializer(),
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            500: "Internal Server Error"
        },
        tags=['market']
    )

    def get(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
            items = OrderItem.objects.filter(order=order)
        except Order.DoesNotExist:
            return Response({'error': 'Pedido não encontrado'}, status=404)

        items_data = DetailOrderItemSerializer(items, many=True)
        order_data = DetailOrderSerializer(order)

        order_data = order_data.data
        order_data['items'] = items_data.data
        return Response(order_data)


class OrderDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Exclui um pedido",
        responses={
            204: "No Content",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            500: "Internal Server Error"
        },
        tags=['market']
    )
    def delete(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
            items = OrderItem.objects.filter(order=order)
        except Order.DoesNotExist:
            return Response({'error': 'Pedido não encontrado'}, status=404)

        items.delete()
        order.delete()

        return Response({'message': 'Pedido excluído com sucesso!'})
