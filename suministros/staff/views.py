from django.shortcuts import render, redirect
from .models import Staff
from .forms import StaffForm
from django.http import HttpResponse

def index(request):
    return render(request, 'staff/index.html', {}) 

def detail(request, id):
    staff = Staff.objects.get(id=id)
    context = {
        'staff': staff,
    }
    # return render(request, 'staff/detail.html', context)
    return HttpResponse('Ver staff en construccion')

def create(request):
    if request.method == 'GET':
        form = StaffForm()
        context = {
            'form': form
        }
        # return render(request, 'staff/create.html', context)
        return HttpResponse('crear staff en construccion')

    if request.method =='POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            return redirect('staff')


def edit(request, id):
    staff = Staff.objects.het(id=id)
    if request.method == 'GET':
        form = StaffForm(instance= staff)
        context = {
            'form': form,
            'id': id,
        }
        return HttpResponse('editar staffo en construccion')


    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'id': id,
            }
        return HttpResponse('editar staffo en construccion')


def delete(request, id):
    staff = Staff.objects.get(id=id)
    staff.delete()
    # return redirect(staff)
    return HttpResponse('eliminar staffo en construccion')