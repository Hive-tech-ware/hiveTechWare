from .models import Order
from rest_framework import serializers
from apps.orderitems.serializers import OrderItemSerializer





class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many = True)
    class Meta: 
        model = Order
        fields = '__all__'
