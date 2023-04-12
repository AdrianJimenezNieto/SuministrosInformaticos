from django.shortcuts import redirect
from .models import Sale
from product.models import Product
from django.contrib.auth.models import User
from cart.models import Cart, CartItem

from django.http import HttpResponse

def sale(request, id_product, id_user):
    user = User.objects.get(id=id_user)
    product = Product.objects.get(id=id_product)
    sale = Sale(user=user, product=product)
    
    sale.save()
        
    return redirect('product')

def saleCart(request, user_id):
    user = User.objects.get(id=user_id)
    cart = Cart.objects.get(user_id=user_id)
    items = CartItem.objects.filter(cart_id=cart.id)

    for item in items:
        sale = Sale(product=item.product, user=user, amount=item.quantity)
        sale.save()
        item.delete()


    return redirect('product')
    