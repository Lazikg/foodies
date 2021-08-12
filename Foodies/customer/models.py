from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, null=True)
    street = models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.user)

class User_payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=150,null=True)
    card_no = models.DecimalField(max_digits=16,decimal_places=1)

    def __str__(self):
        return str(self.card_no)
