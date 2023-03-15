from django.shortcuts import render, redirect
from .models import Costumer
from .forms import CostumerForm
from django.http import HttpResponse

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
        return render(request, 'costumer/create.html', context)

    if request.method =='POST':
        form = CostumerForm(request.POST)
        if form.is_valid():
            return redirect('costumer')


def edit(request, id):
    costumer = Costumer.objects.get(id=id)
    if request.method == 'GET':
        form = CostumerForm(instance= costumer)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, 'costumer/edit.html', context)


    if request.method == 'POST':
        form = CostumerForm(request.POST, instance=costumer)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'id': id,
            }
        return redirect('costumer')


def delete(request, id):
    costumer = Costumer.objects.get(id=id)
    costumer.delete()
    return redirect('costumer')
