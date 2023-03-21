from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterAccessLevelForm

def index(request):
    seleccion = request.POST['accessLevel']
    return HttpResponse(seleccion)

def registerAccessLevel(request):
    return render(request, 'register/accessLevel.html', {'form': RegisterAccessLevelForm()})
