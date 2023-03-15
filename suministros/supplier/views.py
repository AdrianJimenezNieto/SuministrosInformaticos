from django.shortcuts import render, redirect
from .models import Supplier
from .forms import SupplierForm

def index(request):
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers,
    }
    return render(request, 'supplier/index.html', context) 

def detail(request, id):
    supplier = Supplier.objects.get(id=id)
    context = {
        'supplier': supplier,
    }
    return render(request, 'supplier/detail.html', context)

def create(request):
    if request.method == 'GET':
        form = SupplierForm()
        context = {
            'form': form
        }
        return render(request, 'supplier/create.html', context)

    if request.method =='POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            return redirect('supplier')


def edit(request, id):
    supplier = Supplier.objects.get(id=id)
    if request.method == 'GET':
        form = SupplierForm(instance= supplier)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, 'supplier/edit.html', context)


    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'id': id,
            }
        return redirect('supplier')


def delete(request, id):
    supplier = Supplier.objects.get(id=id)
    supplier.delete()
    return redirect('supplier')
