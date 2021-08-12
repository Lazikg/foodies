from .models import OrderItem, Orders
from django.forms import fields, forms
from django import forms

class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderCreate(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

# class CartCreate(forms.ModelForm):
#     class Meta:
#         model = Cart_details
#         fields = '__all__'