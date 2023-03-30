from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Cart, CartItem

def index(request):
    return render(request, 'cart/index.html', {})

##-------------- Cart Views --------------------------------------
class DetailCart(DetailView):
    model = Cart
    template_name='cart/detail-cart.html'

class ListCart(ListView):
    model = Cart
    context_object_name = 'carts'
    template_name='cart/list-carts.html'

class CreateCart(CreateView):
    model = Cart
    template_name = 'cart/create-cart.html'

class Updatecart(UpdateView):
    model = Cart
    template_name = 'cart/update-cart.html'

class DeleteCart(DeleteView):
    model = Cart
    template_name = 'cart/delete-cart.html'


##-------------- CartItem Views --------------------------------------
class DetailCartItem(DetailView):
    model = CartItem
    template_name='cartitem/detail-cartitem.html'

class ListCartItem(ListView):
    model = CartItem
    context_object_name = 'cartitems'
    template_name='cartitem/list-cartitems.html'

class CreateItemCart(CreateView):
    model = CartItem
    template_name = 'cartitem/create-cartitem.html'

class UpdateCartItem(UpdateView):
    model = CartItem
    template_name = 'cartitem/update-cartitem.html'

class DeleteCartItem(DeleteView):
    model = Cart
    template_name = 'cartitem/delete-cartitem.html'