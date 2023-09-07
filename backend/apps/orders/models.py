from django.db import models
from apps.users.models import Users

# Create your models here.

class Order (models.Model):
    class Meta(object):
        db_table = 'order'

    user = models.ForeignKey(
        Users, related_name= 'related_user_order', on_delete = models.CASCADE
    )

    customer_name = models.CharField(
        'customer_name', blank= False, null= False, max_length= 20
    )

    customer_phone = models.IntegerField(
        'customer_phone', max_length=15, blank= False, null= False
    )

    address = models.CharField(
        'address', blank= False, null=False, max_length=205
    )

    zip_code = models.IntegerField(
        'zip_code', blank= False, null= False, max_length=5
    )

    apt =  models.CharField(
        'apt', blank=False, null=False, max_length=20
    )

    city = models.CharField(
        'city', blank=False, null=False, max_length= 20
    )

    state = models.CharField(
        'state', blank= False, null=False, max_length= 10
    )

    total_price = models.FloatField(
        'total_price', blank= False, null=False,
    )

    total_quantity = models.IntegerField(
        'total_quantity', blank=False, null=False,
    )

    def order_items(self):
        return self.related_order.all()