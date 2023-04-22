from django.shortcuts import render, redirect
from .models import Costumer
from .forms import CostumerForm, UpdateCostumerForm, UpdatePasswordCostumerForm
from django.contrib import messages

def index(request):
    costumers = Costumer.objects.all()
    context = {
        'costumers': costumers,
    }
    return render(request, 'costumer/index.html', context) 

def detail(request, id):
    costumer = Costumer.objects.get(id=id)
    context = {
        'costumer': costumer,
    }
    return render(request, 'costumer/detail.html', context)

def create(request):
    if request.method == 'GET':
        form = CostumerForm()
        context = {
            'form': form
        }
        messages.add_message(request, messages.INFO, "USUARIO CREADO SATISFACTORIAMENTE")
        return render(request, 'costumer/create.html', context)

    if request.method =='POST':
        form = CostumerForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.INFO, "USUARIO CREADO SATISFACTORIAMENTE")
            return redirect('costumer')


def edit(request):
    costumer = request.user.costumer
    if request.method == 'GET':
        form = UpdateCostumerForm(instance=costumer)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, 'costumer/edit.html', context)


    if request.method == 'POST':
        form = UpdateCostumerForm(request.POST, instance=costumer)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "PERFIL EDITADO SATISFACTORIAMENTE")
            return redirect('index')
        else:
            messages.add_message(request, messages.INFO, "HA HABIDO UN PROBLEMA AL EDITAR EL PERFIL")
            return redirect('index')
        
def updatePassword(request):
    
    if request.method == 'GET':
        form = UpdatePasswordCostumerForm(request.user)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, 'costumer/updatePassword.html', context)


    if request.method == 'POST':
        form = UpdatePasswordCostumerForm(user=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "CONTRASEÑA ACTUALIZADA")
            return redirect('index')
        else:
            return redirect('index')

def delete(request):
    request.user.costumer.delete()
    
    messages.add_message(request, messages.INFO, "USUARIO BORRADO")
    return redirect('costumer')
