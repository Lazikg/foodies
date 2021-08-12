from typing import cast
from django.http.request import validate_host
from django.shortcuts import render, redirect, reverse
from django.utils.translation import activate
from .models import Product, Category
from django.views import View
from django.utils.datastructures import MultiValueDictKeyError
from Cart.forms import CartAddProductForm
from django.conf import settings
# Create your views here.

class Home(View):

    def get(self, request, *args, **kwargs):
        
        return render(request, 'Foods/index.html')

    def post(self, request):
        current_lang = request.POST.get('language')
        if current_lang == settings.LANGUAGES[0][0]:
            reverse('home')
            activate('en')
        elif current_lang == settings.LANGUAGES[0][1]:
            reverse('home')
            activate('uz')

        return render(request, 'Foods/index.html')


class About(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'Foods/about.html')


class Contact(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'Foods/contact.html')


class Category_Products(View):
    def get(self, request, cid, *args, **kwargs):
        product = Product.objects.filter(category=cid)
        category = Category.objects.all()
        cart_product_form = CartAddProductForm()
        context = {
            'category':category,
            'product':product,
            'cart_product_form':cart_product_form,
            }
        return render(request, 'Foods/menu.html', context)


class Products(View):
    def get(self, request):
        products = Product.objects.all()
        category = Category.objects.all()
        cart_product_form = CartAddProductForm()

        context = {
            'category':category,
            'products':products,
            'cart_product_form':cart_product_form,

        }
        return render(request, 'Foods/menu.html', context)
    
