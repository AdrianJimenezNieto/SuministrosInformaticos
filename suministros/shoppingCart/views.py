from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return render(request, 'cart/index.html', {})
    return HttpResponse('indice carrito de la compra (EN CONSTRUCCION)')

def add(request, id):
    # return render(request, 'cart/index.html', {})
    return HttpResponse('añadir carrito de la compra (EN CONSTRUCCION)')

def delete(request, id):
    # return render(request, 'cart/index.html', {})
    return HttpResponse('borrar carrito de la compra (EN CONSTRUCCION)')