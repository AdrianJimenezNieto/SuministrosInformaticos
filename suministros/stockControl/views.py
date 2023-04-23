from django.shortcuts import render, redirect
from .models import StockControl
from product.models import Product
from sale.models import SupplierSale
from django.contrib import messages

def stockControl (request):
    stockControl = StockControl.objects.all()
    context = {
        'stockControl': stockControl,
    }

    return render(request, 'stockControl/stockControl.html', context)

def buyStock(request, stockControl_id):

    stockControl = StockControl.objects.get(id=stockControl_id)
    product = Product.objects.get(id=stockControl.product.id)
    supplierSale = SupplierSale(product=product, supplier=product.supplier, amount=product.minStock-product.stock)


    product.stock = product.minStock
    
    supplierSale.save()
    stockControl.delete()
    product.save()

    messages.add_message(request, messages.INFO, "STOCK COMPRADO AL PROVEEDOR")
    return redirect('stockControl')
