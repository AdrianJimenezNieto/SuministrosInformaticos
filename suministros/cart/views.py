from django.shortcuts import render
from django.http import HttpResponse

def cart(request):
    return HttpResponse('estoy en el carro')