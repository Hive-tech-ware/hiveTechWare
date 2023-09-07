from .models import Products
from rest_framework import serializers
from apps.categories.serializers import CategorySerializer



class ProductSerializer(serializers.ModelSerializer):
    product_img = serializers.ImageField(read_only = True)
    category =  CategorySerializer(read_only = True, many = False)

    class Meta:
        model = Products
        fields = '__all__'
        depth = 1

        