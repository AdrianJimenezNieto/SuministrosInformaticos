from django.shortcuts import render
from sale.models import Sale, SupplierSale
from django.contrib.auth.models import User

def graphs(request, graph=None, user_id=None):
    if graph != None:
        if graph == 'costumer':
            sales = Sale.objects.all()
            context = {
                'graph': 'costumer',
                'sales': sales, 
            }
            return render(request, 'graphs/graphs.html', context)
        if graph == 'supplier':
            sales = SupplierSale.objects.filter(supplier_id=User.objects.get(id=user_id))
            context = {
                'graph': 'supplier', 
            }
            return render(request, 'graphs/graphs.html', context)            
    return render(request, 'graphs/graphs.html', {})
