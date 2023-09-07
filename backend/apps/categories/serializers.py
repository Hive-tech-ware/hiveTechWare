from rest_framework.fields import ImageField
from .models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    image = ImageField(read_only = True)
    class Meta:
        model = Category
        fields = '__all__'

        