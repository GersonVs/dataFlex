from rest_framework import serializers
from .models import Product, Order, OrderItem
from apps.consumer.models import Client, ClientAddress

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'unity_measure')

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ('product', 'product_name', 'quantity')

class OrderSerializer(serializers.Serializer):
    client_id = serializers.IntegerField()
    client_address_id = serializers.IntegerField()
    items = OrderItemSerializer(many=True)

    def get_items(self, order):
        items = OrderItem.objects.filter(order=order)
        serializer = OrderItemSerializer(items, many=True)
        return serializer.data

    def create(self, validated_data):
        client_id = validated_data['client_id']
        client_address_id = validated_data['client_address_id']
        items_data = validated_data['items']

        # Obter informações do cliente e endereço
        client = Client.objects.get(id=client_id)
        client_address = ClientAddress.objects.get(id=client_address_id)

        # Calcular valores totais
        total_value = 0
        for item_data in items_data:
            product_id = item_data['product'].id
            quantity = item_data['quantity']
            product = Product.objects.get(id=product_id)
            total_value += product.price * quantity

        # Criar pedido
        order = Order.objects.create(client=client, client_address=client_address, total_value=total_value)

        # Criar itens do pedido
        for item_data in items_data:
            product_id = item_data['product'].id
            quantity = item_data['quantity']
            product = Product.objects.get(id=product_id)
            total_value = product.price * quantity
            OrderItem.objects.create(order=order, product=product, quantity=quantity, total_value=total_value)

        return order