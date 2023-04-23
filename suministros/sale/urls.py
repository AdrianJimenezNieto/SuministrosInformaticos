from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('product/<str:id_product>/', views.sale, name='sales'),
    path('cart/', views.saleCart, name='saleCart'),
]