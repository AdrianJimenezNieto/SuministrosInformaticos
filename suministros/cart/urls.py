from django.urls import path

from . import views

urlpatterns = [
    path('', views.viewCart, name='cart'),
    path('add/<int:product_id>/', views.addToCart, name='addToCart'),
    path('delete/<int:item_id>/', views.delFromCart, name='delFromCart'),
]
