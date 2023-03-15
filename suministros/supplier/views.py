from django.shortcuts import render, redirect
from .models import Supplier
from .forms import SupplierForm
from django.http import HttpResponse

def index(request):
    return render(request, 'supplier/index.html', {}) 

def detail(request, id):
    supplier = Supplier.objects.get(id=id)
    context = {
        'supplier': supplier,
    }
    # return render(request, 'supplier/detail.html', context)
    return HttpResponse('Ver supplier en construccion')

def create(request):
    if request.method == 'GET':
        form = SupplierForm()
        context = {
            'form': form
        }
        # return render(request, 'supplier/create.html', context)
        return HttpResponse('crear supplier en construccion')

    if request.method =='POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            return redirect('supplier')


def edit(request, id):
    supplier = supplier.objects.het(id=id)
    if request.method == 'GET':
        form = SupplierForm(instance= supplier)
        context = {
            'form': form,
            'id': id,
        }
        return HttpResponse('editar suppliero en construccion')


    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'id': id,
            }
        return HttpResponse('editar suppliero en construccion')


def delete(request, id):
    supplier = Supplier.objects.get(id=id)
    supplier.delete()
    # return redirect(supplier)
    return HttpResponse('eliminar suppliero en construccion')