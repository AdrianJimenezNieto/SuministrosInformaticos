from django.shortcuts import render
from .forms import LoginForm
from costumer.models import Costumer
from staff.models import Staff
from supplier.models import Supplier
from django.http import HttpResponse

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        if validateUser(request.POST['username'], request.POST['password'], request.POST['accessLevel']):
            accessLevel = int(request.POST['accessLevel'])
            return render(request, 'index.html', {'accessLevel': accessLevel})
        return render(request, 'login/login.html', {'form': form})
        
    if request.method == 'GET':
        return render(request, 'login/login.html', {'form': form})

def validateUser(username, password, accessLevel):
    if int(accessLevel) == 1:
        for costumer in Costumer.objects.all():
            if costumer.username == username:
                if costumer.password == password:
                    return True

    elif int(accessLevel) == 2:
        for supplier in Supplier.objects.all():
            if supplier.username == username:
                if supplier.password == password:
                    return True

    else:
        for staff in Staff.objects.all():
            if staff.username == username:
                if staff.password == password:
                    return True
    
    return False