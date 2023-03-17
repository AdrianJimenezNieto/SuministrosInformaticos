from django.shortcuts import render
from django.http import HttpResponse
from .models import ShoppingCart
from product.models import Product
from costumer.models import Costumer

def index(request):
    # return render(request, 'cart/index.html', {})
    return HttpResponse('indice carrito de la compra (EN CONSTRUCCION)')

def add(request, id):
    # return render(request, 'cart/index.html', {})
    user = Costumer.objects.get(id=83)
    product = Product.objects.get(id=54)
    carrito = ShoppingCart()
    carrito.user = user
    carrito.product = product
    carrito.amount = 5
    carrito.save()

    result = user.shoppingcart_set.all()

    return HttpResponse(result.product)

def delete(request, id):
    # return render(request, 'cart/index.html', {})
    return HttpResponse('borrar carrito de la compra (EN CONSTRUCCION)')