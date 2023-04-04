from rest_framework import serializers
from .models import Product, Order, OrderItem
from apps.consumer.models import Client, ClientAddress

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'unity_measure')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product', 'quantity')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['client', 'client_address', 'items']

class DetailOrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'total_value')

class DetailOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'date', 'client', 'client_address', 'total_value']