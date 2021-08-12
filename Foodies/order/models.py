from django.db import models
from Foods.models import Product

# Create your models here


class OrderItem(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=13, null=True)
    street = models.CharField(max_length=500, null=True)   
    create_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.phone)

class OrderProudcts(models.Model):
    products = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True)
    quantity = models.FloatField(null=True)
    total = models.DecimalField(max_digits=100,decimal_places=2, null=True)

    def __str__(self):
        return self.total

class Orders(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    card_type = models.CharField(max_length=100, default='Card type', null=True)
    card_number = models.CharField(max_length=16,null=True)
    exp_date = models.CharField(max_length=100, null=True)
    paid = models.BooleanField()
    orer_product = models.ForeignKey(OrderProudcts, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True,null=True)
    order_number = models.IntegerField(default=1)

    def __str__(self):
        return str(self.order_number)
