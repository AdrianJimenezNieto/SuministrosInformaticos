from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

@login_required(login_url='/register/login')
def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product/index.html', context) 

def detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product,
    }
    return render(request, 'product/detail.html', context)

def create(request):
    if request.method == 'GET':
        form = ProductForm()
        context = {
            'form': form
        }
        return render(request, 'product/create.html', context)

    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            return redirect('product')


def edit(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'GET':
        form = ProductForm(instance= product)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, 'product/edit.html', context)


    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'id': id,
            }
        return redirect('product')


def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product')
