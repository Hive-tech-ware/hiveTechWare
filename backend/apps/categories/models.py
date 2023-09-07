from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Category(models.Model):
    class Meta (object):
        db_table = 'category'

    name =  models.CharField(
        'name', blank= False, null= False, max_length= 20
    )

    image = CloudinaryField(
        blank= True, null= True
    )

    created_at = models.DateTimeField(
      'created_at', blank= True, auto_now_add= True  
    )

    updated_at = models.DateTimeField(
        'updated_at', blank= True, auto_now_add= True
    )

    def __str__(self):
        return self.name