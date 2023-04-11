from django.shortcuts import render, redirect
from .models import Cart, CartItem
from product.models import Product
from django.contrib.auth.models import User

from django.http import HttpResponse

def viewCart(request, id):

    if id in Cart.objects.values_list('user_id', flat=True):
        cart = Cart.objects.get(user_id=id)

    else:
        cart = Cart(user=User.objects.get(id=id))
        cart.save()

    items = CartItem.objects.filter(cart_id=cart.id)
    context = {
        'items': items,
    }

    return render(request, 'cart/cartItems.html', context)

def addToCart(request, product_id, user_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(user_id=user_id)
    cartItem = CartItem()

    return redirect(viewCart)

def delFromCart(requets, id):
    return 


