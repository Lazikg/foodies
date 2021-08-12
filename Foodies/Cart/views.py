from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Foods.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    products = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=products,
            quantity=cd['quantity'],
            override_quantity=cd['override'])
    return redirect('card:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)    
    return redirect('card:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:   
        item['update_quantity_form'] = CartAddProductForm(initial={
                                                        'quantity': item['quantity'],
                                                        'override': True})
    context =  {'cart1': cart}
    return render(request, 'cart/detail.html', context)
    # return render(request, 'foods/menu.html', context)

