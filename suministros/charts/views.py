from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from costumer.models import Costumer
from supplier.models import Supplier
from sale.models import Sale, SupplierSale
from datetime import datetime

def chart(request, user_id, chartType=None):
    user = User.objects.get(id=user_id)
    context = {}

    try:
        if isinstance(user.costumer, Costumer):
            context = {
                'access': 1,
            }
            if chartType != None:
                dataX, dataY = getData(Sale.objects.filter(user_id=user.id), chartType)
                context['chartLabel'] = 'buys'
                context['chart'] = True
                context['dataX'] = dataX
                context['dataY'] = dataY
    except Exception:
        pass

    try:    
        if isinstance(user.supplier, Supplier):
            context = {
                'access': 2
            }
            if chartType != None:
                print(user.id)
                dataX, dataY = getData(SupplierSale.objects.filter(supplier_id=user.id), chartType)
                context['chartLabel'] = 'sale'
                context['chart'] = True
                context['dataX'] = dataX
                context['dataY'] = dataY
    except Exception:
        pass

    if user.is_staff == True:
        context = {
                'access': 3
            }
        if chartType != None:
                if chartType == 'salesPerDate':
                    dataX, dataY = getData(Sale.objects.all(), chartType)
                    context['chartLabel'] = 'sale'
                elif chartType == 'salesPerProduct':
                    dataX, dataY = getData(Sale.objects.all(), chartType)
                    context['chartLabel'] = 'sale'
                elif chartType == 'salesPerDateSupplier':
                    dataX, dataY = getData(SupplierSale.objects.all(), chartType)
                    context['chartLabel'] = 'buys'
                elif chartType == 'salesPerProductSupplier':
                    dataX, dataY = getData(SupplierSale.objects.all(), chartType)
                    context['chartLabel'] = 'buys'
                
                print(dataX, dataY)
                context['chart'] = True
                context['dataX'] = dataX
                context['dataY'] = dataY
                
        
    return render(request, 'charts/charts.html', context)

def getData(data, chartType):
    dataX = []
    dataY = []

    if chartType == 'salesPerDate':
        for item in data:
            if item.date in dataX:
                dataY[dataX.index(item.date)] += item.amount
            else:
                dataX.append(item.date)
                dataY.append(item.amount)

    if chartType == 'salesPerProduct':
        for item in data:
            if item.product in dataX:
                dataY[dataX.index(item.product)] += item.amount
            else:
                dataX.append(item.product)
                dataY.append(item.amount)

    if chartType == 'salesPerDateSupplier':
        for item in data:
            if item.date in dataX:
                dataY[dataX.index(item.date)] += item.amount
            else:
                dataX.append(item.date)
                dataY.append(item.amount)

    if chartType == 'salesPerProductSupplier':
        for item in data:
            if item.product in dataX:
                dataY[dataX.index(item.product)] += item.amount
            else:
                dataX.append(item.product)
                dataY.append(item.amount)

    return dataX, dataY
