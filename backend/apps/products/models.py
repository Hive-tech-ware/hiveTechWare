from django.db import models
from cloudinary.models import CloudinaryField
from apps.categories.models import Category

# Create your models here.

PRODUCT_TYPE = (
    ('male','Male'),
    ('female','Female')
)

class Products (models.Model):
    class Meta (object):
        db_table = 'products'
    
    name = models.CharField(
        'Name', max_length= 20, blank= False, null= False
    )

    description = models.CharField(
        'Description', blank  =  False, null = False, max_length= 120
    )

    price = models.CharField(
        'Price', blank= False, null=False, max_length=10
    )

    product_img = CloudinaryField(
        'Product Img', null = True, blank = True
    )

    type = models.CharField(
        'Type', choices= PRODUCT_TYPE, blank=False, null=False, max_length= 20
    )

    category = models.ForeignKey(
        Category, on_delete= models.CASCADE, related_name= 'related_category'
    )

    
    def __str__(self):
        return (self.name)


