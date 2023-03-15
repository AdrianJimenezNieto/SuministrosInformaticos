from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse

def index(request):
    return render(request, 'product/index.html', {}) 

def detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product,
    }
    # return render(request, 'product/detail.html', context)
    return HttpResponse('Ver producto en construccion')

def create(request):
    if request.method == 'GET':
        form = ProductForm()
        context = {
            'form': form
        }
        # return render(request, 'product/create.html', context)
        return HttpResponse('crear producto en construccion')

    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            return redirect('product')


def edit(request, id):
    product = Product.objects.het(id=id)
    if request.method == 'GET':
        form = ProductForm(instance= product)
        context = {
            'form': form,
            'id': id,
        }
        return HttpResponse('editar producto en construccion')


    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'id': id,
            }
        return HttpResponse('editar producto en construccion')


def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    # return redirect(product)
    return HttpResponse('eliminar producto en construccion')