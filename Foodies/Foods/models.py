from django.db import models
from django.db.models.base import Model

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    image_nav = models.ImageField(upload_to='nav_logos/')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)    
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    desc = models.TextField(max_length=100,null=True)
    image = models.ImageField(upload_to='media/menu_images/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

