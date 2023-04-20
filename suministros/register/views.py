from django.shortcuts import render, redirect
from .forms import RegisterAccessLevelForm
from costumer.forms import CostumerForm
from supplier.forms import SupplierForm
from staff.forms import StaffForm
from django.contrib.auth import login
from django.contrib import messages

def signUp(request, acceso):
    if request.method == 'POST':
        if int(acceso) == 1:
            form = CostumerForm(request.POST)
        if int(acceso) == 2:
            form = SupplierForm(request.POST)
        if int(acceso) == 3:
            form = StaffForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.add_message(request, messages.INFO, "SESION INICIADA")
            return redirect('/')
        
        else:
            messages.add_message(request, messages.INFO, "ERROR EN EL INICIO DE LA SESION")
            return redirect('index')
        
    if request.method == 'GET':
        if int(acceso) == 1:
            form = CostumerForm()
        if int(acceso) == 2:
            form = SupplierForm()
        if int(acceso) == 3:
            form = StaffForm()

        return render(request, 'registration/SignUp.html', {'form': form, 'acceso': acceso})
    
    
def seleccionarAcceso(request):
    if request.method == 'POST':
        return redirect('signUp', acceso= request.POST['acceso'])

    if request.method == 'GET':
        form = RegisterAccessLevelForm()
        return render(request, 'registration/select.html', {'form': form})