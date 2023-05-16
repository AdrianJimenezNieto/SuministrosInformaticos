from django.shortcuts import redirect
from .models import Sale
from product.models import Product
from cart.models import Cart, CartItem
from stockControl.models import StockControl
from django.contrib import messages

def sale(request, id_product):
    product = Product.objects.get(id=id_product)
    if product.stock >= 1:
        product.stock -= 1
        sale = Sale(user=request.user, product=product)
        
        product.save()
        sale.save()

        if product.stock < 0.9 * product.minStock:
            if product.id in StockControl.objects.values_list('product_id', flat=True):
                pass
            else:
                stockControl = StockControl(product=product)
                stockControl.save()

        messages.add_message(request, messages.INFO, "PRODUCTO COMPRADO")

    else:
        messages.add_message(request, messages.INFO, "STOCK INSUFICIENTE DEL PRODUCTO {}".format(product.name))

    return redirect('product')

def saleCart(request):
    cart = Cart.objects.get(user_id=request.user.id)
    items = CartItem.objects.filter(cart_id=cart.id)

    for item in items:
        product = item.product
        sale = Sale(product=item.product, user=request.user, amount=item.quantity)
        if product.stock >= sale.amount:
            product.stock -= sale.amount

            if product.stock < 0.9 * product.minStock:
                stockControl = StockControl(product=product)
                stockControl.save()

            product.save()
            sale.save()
            item.delete()
        else:
            messages.add_message(request, messages.INFO, "STOCK INSUFICIENTE DEL PRODUCTO {}".format(product.name))

    messages.add_message(request, messages.INFO, "COMPRADO TODOO EL CARRITO")
    return redirect('product')
    