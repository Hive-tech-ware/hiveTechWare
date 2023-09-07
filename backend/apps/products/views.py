from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Products
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.

class ProductList(generics.ListAPIView):
    queryset =  Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['type','category_id']
    search_fields = ['name','description']