from django.shortcuts import render
from .models import StockControl

def stockControl (request):
    stockControl = StockControl.objects.all()
    context = {
        'stockControl': stockControl,
    }

    return render(request, 'stockControl/stockControl.html', context)