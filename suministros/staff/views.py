from django.shortcuts import render, redirect
from .models import Staff
from .forms import StaffForm, UpdateStaffForm, UpdatePasswordStaffForm
from django.contrib import messages

def index(request):
    staffs = Staff.objects.all()
    context = {
        'staffs': staffs,
    }
    return render(request, 'staff/index.html', context) 

def detail(request):
    staff = Staff.objects.get(id=id)
    context = {
        'staff': staff,
    }
    return render(request, 'staff/detail.html', context)


def edit(request):
    if request.method == 'GET':
        form = UpdateStaffForm(instance=request.user)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, 'staff/edit.html', context)


    if request.method == 'POST':
        form = UpdateStaffForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "PERFIL ACTUALIZADO")
            return redirect('index')
        else:
            messages.add_message(request, messages.INFO, "ERROR AL ACTUALIZAR EL PERFIL")
            return redirect('index')
        
def updatePassword(request):
    
    if request.method == 'GET':
        form = UpdatePasswordStaffForm(request.user)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, 'staff/updatePassword.html', context)


    if request.method == 'POST':
        form = UpdatePasswordStaffForm(user=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "CONTRASEÑA ACTUALIZADA")
            return redirect('index')
        else:
            messages.add_message(request, messages.INFO, "ERROR AL ACTUALIZAR LA CONTRASEÑA")
            return redirect('index')


def delete(request):
    staff = request.user.staff
    staff.delete()

    messages.add_message(request, messages.INFO, "USUARIO BORRADO")
    return redirect('staff')
