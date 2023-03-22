from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterAccessLevelForm
from costumer.forms import CostumerForm
from supplier.forms import SupplierForm
from staff.forms import StaffForm

def index(request):
    if request.method == 'POST':
        if int(request.POST['accessLevel']) == 1:
            form = CostumerForm()
            return render(request, 'register/createCostumer.html', {'form': form})

        if int(request.POST['accessLevel']) == 2:
            form = SupplierForm()
            return render(request, 'register/createSupplier.html', {'form': form})

        if int(request.POST['accessLevel']) == 3:
            form = StaffForm()
            return render(request, 'register/createStaff.html', {'form': form})
    
    if request.method == 'GET':
        return render(request, 'register/index.html', {'form': RegisterAccessLevelForm()})

