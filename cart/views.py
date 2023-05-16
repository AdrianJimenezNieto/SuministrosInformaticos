from django.shortcuts import render, redirect
from .models import Cart, CartItem
from django.contrib import messages

def viewCart(request,):

    if request.user.id in Cart.objects.values_list('user_id', flat=True):
        cart = Cart.objects.get(user_id=request.user.id)

    else:
        cart = Cart(user=request.user)
        cart.save()

    items = CartItem.objects.filter(cart_id=cart.id)
    context = {
        'items': items,
    }

    return render(request, 'cart/cartItems.html', context)

def addToCart(request, product_id):
    if request.user.id in Cart.objects.values_list('user_id', flat=True):
        cart = Cart.objects.get(user_id=request.user.id)
    else:
        cart = Cart(user=request.user)
        cart.save()

    if product_id in CartItem.objects.filter(cart_id=cart.id).values_list('product_id', flat=True):
        item = CartItem.objects.get(cart_id=cart.id, product_id=product_id)
        item.quantity += 1
    else:
        item = CartItem(cart_id=cart.id, product_id=product_id)

    item.save()

    messages.add_message(request, messages.INFO, "PRODUCTO AÑADIDO AL CARRITO")
    return redirect('product')

def delFromCart(request, item_id):
    item = CartItem.objects.get(id=item_id)
    item.delete()

    messages.add_message(request, messages.INFO, "PRODUCTO QUITADO DEL CARRITO")
    return redirect('cart')


