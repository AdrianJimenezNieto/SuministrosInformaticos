from django.shortcuts import render, redirect
from .models import Staff
from .forms import StaffForm
from django.http import HttpResponse

def index(request):
    staffs = Staff.objects.all()
    context = {
        'staffs': staffs,
    }
    return render(request, 'staff/index.html', context) 

def detail(request, id):
    staff = Staff.objects.get(id=id)
    context = {
        'staff': staff,
    }
    return render(request, 'staff/detail.html', context)

def create(request):
    if request.method == 'GET':
        form = StaffForm()
        context = {
            'form': form
        }
        return render(request, 'staff/create.html', context)

    if request.method =='POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            return redirect('staff')


def edit(request, id):
    staff = Staff.objects.get(id=id)
    if request.method == 'GET':
        form = StaffForm(instance= staff)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, 'staff/edit.html', context)


    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'id': id,
            }
        return redirect('staff')


def delete(request, id):
    staff = Staff.objects.get(id=id)
    staff.delete()
    return redirect('staff')
