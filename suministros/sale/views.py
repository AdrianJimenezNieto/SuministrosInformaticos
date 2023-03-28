from django.shortcuts import redirect
from .models import Sale
from product.models import Product
from django.contrib.auth.models import User

def sale(request, id_product, id_user):
    user = User.objects.get(id=id_user)
    product = Product.objects.get(id=id_product)
    sale = Sale(user=user, product=product)
    
    sale.save()
        
    return redirect('product')
    