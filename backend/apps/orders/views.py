from django.shortcuts import render
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer,OrderListSerializer


# Create your views here.

class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def get(self,request,*args,**kwargs):
        self.queryset = Order.objects.order_by('-id').filter(user=request.login_user.id)
        return self.list(request, *args, **kwargs)


class OrderAdd(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def post(self,request,*args,**kwargs):
        request.data['user'] = request.login_user.id
        return super().create(request,*args,**kwargs)