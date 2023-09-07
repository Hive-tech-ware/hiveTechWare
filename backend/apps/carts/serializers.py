from rest_framework import serializers
from .models import Cart
from apps.users.serializers import UserSerializer
from apps.products.serializers import ProductSerializer

class CartListSerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = Cart
        fields = '__all__'
        depth = 1


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    def validate(self , data):
        errors = {}
        if 'quantity' not in data or not data['quantity']:
            errors['quantity'] =  ['Quantity is required']

        if 'products' not in data or not data["products"]:
            errors['products'] = ['Product is required']

        if bool(errors):
            raise serializers.ValidationError(errors)
        
        return data

class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    def validate(self , data):
        errors = {}
        if 'quantity' not in data or not data['quantity']:
            errors['quantity'] =  ['Quantity is required']

        if bool(errors):
            raise serializers.ValidationError(errors)
        
        return data
