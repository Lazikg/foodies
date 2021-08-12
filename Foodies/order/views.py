from order.forms import OrderCreate
from django.http.response import HttpResponseNotFound
from django.shortcuts import redirect, render, reverse
from Cart.cart import Cart
from .models import *
from django.contrib import messages
from datetime import datetime
from random import random, randint
# Create your views here.

def order(request):
    date_format = "%Y-%m-%d"
    cart = Cart(request)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        OrderItem.objects.create(name=name,phone=phone,street=address)
        x = OrderItem.objects.create(name=name,phone=phone,street=address)
        get_orderitem = OrderItem.objects.filter(phone=phone)
        # orders model
        card_number = request.POST.get('card_number')
        exp_date = request.POST.get('exp_date')
        card_type = request.POST.get('card_type')
        check_date = datetime.strptime(str(exp_date), date_format)
        day_str = datetime.today().strftime('%Y-%m-%d')
        current_day = datetime.strptime(str(day_str), date_format)
        if check_date < current_day:
            messages.warning(request, "Please enter valid dates!")
            return redirect('order:payment')
        else:
            order_number = randint(1,100)

            for item in cart:
                d = OrderProudcts.objects.create(products=item['product'],
                                    quantity=item['quantity'],
                                    total=item['total_price']
                                    )
                OrderProudcts.objects.create(products=item['product'],
                                    quantity=item['quantity'],
                                    total=item['total_price']
                                    )
                
            cart.clear()
            Orders.objects.create(order_item=x,card_type=card_type, card_number=card_number, exp_date=exp_date,order_number=order_number,orer_product=d)
            request.session['order_number'] = order_number
            return redirect('order:thanks')
   
    return render(request, 'order/order.html',{'cart1':cart })

def thx(request):
    cart = Cart(request)
    return render(request, 'order/thx.html',{'cart':cart})