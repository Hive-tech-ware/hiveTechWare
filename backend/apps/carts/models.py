from django.db import models
from apps.users.models import Users
from apps.products.models import Products

# Create your models here.

class Cart(models.Model):
    class Meta(object):
        db_table = 'carts'

    
    user = models.ForeignKey(
        Users, related_name= 'related_user', on_delete=models.CASCADE
    )

    products = models.ForeignKey(
        Products, related_name= 'related_products', on_delete=models.CASCADE
    )

    quantity = models.IntegerField(
        'quantity', blank=False, null=False
    )


    @property
    def total_price(self):
        return self.quantity * self.products.price