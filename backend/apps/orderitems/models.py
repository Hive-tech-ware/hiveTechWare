from django.db import models
from apps.products.models import Products
from apps.orders.models import Order
from django.utils import timezone

# Create your models here.

class OrderItem(models.Model):
    class Meta (object):
        db_table = 'orderitems'

    product =  models.ForeignKey(
        Products, related_name= 'related_product', on_delete= models.CASCADE
    )

    order =  models.ForeignKey(
        Order, related_name='related_order', on_delete= models.CASCADE
    )

    quantity = models.IntegerField(
        'quantity' , blank= False, null= False
    )

    created_at = models.DateTimeField(
        'created_at' ,  blank=True, default= timezone.now
    )
    
