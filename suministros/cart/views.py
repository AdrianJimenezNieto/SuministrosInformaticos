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
    if user_id in Cart.objects.values_list('user_id', flat=True):
        cart = Cart.objects.get(user_id=user_id)
        
    else:
        cart = Cart(user=User.objects.get(id=user_id))
        cart.save()

    item = CartItem(cart_id=cart.id, product_id=product_id)
    item.save()

    return redirect('index')

def delFromCart(requets, item_id, user_id):
    item = CartItem.objects.get(id=item_id)
    item.delete()

    return redirect('cart', id=user_id)


