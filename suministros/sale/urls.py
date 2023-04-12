from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:id_product><str:id_user>/', views.sale, name='sales'),
    path('cart/<int:user_id>/', views.saleCart, name='saleCart'),
]

