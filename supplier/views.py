from django.shortcuts import render, redirect
from .models import Supplier
from .forms import SupplierForm, UpdateSupplierForm, UpdatePasswordSupplierForm
from django.contrib import messages

def index(request):
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers,
    }
    return render(request, 'supplier/index.html', context) 

def detail(request):
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
            messages.add_message(request, messages.INFO, "USUARIO CREADO")
            return redirect('supplier')
        else:
            messages.add_message(request, messages.INFO, "ERROR AL CREAR EL PERFIL")
            return redirect('index')


def edit(request):
    if request.method == 'GET':
        form = UpdateSupplierForm(instance=request.user)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, 'supplier/edit.html', context)


    if request.method == 'POST':
        form = UpdateSupplierForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "PERFIL ACTUALIZADO")
            return redirect('index')
        else:
            messages.add_message(request, messages.INFO, "ERROR AL ACTUALIZAR EL PERFIL")
            return redirect('index')
        
def updatePassword(request):
    
    if request.method == 'GET':
        form = UpdatePasswordSupplierForm(request.user)
        context = {
            'form': form,
            'id': id,
        }
        
        return render(request, 'supplier/updatePassword.html', context)


    if request.method == 'POST':
        form = UpdatePasswordSupplierForm(user=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "CONTRASEÑA ACTUALIZADA")
            return redirect('index')
        else:
            messages.add_message(request, messages.INFO, "ERROR AL ACTUALIZAR LA CONTRASEÑA")
            return redirect('index')


def delete(request):
    supplier = Supplier.objects.get(id=id)
    supplier.delete()

    messages.add_message(request, messages.INFO, "USUARIO BORRADO")
    return redirect('supplier')
