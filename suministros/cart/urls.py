from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.viewCart, name='cart'),
    path('add/<int:id>/', views.addToCart, name='addToCart'),
    path('delete/<int:id>/', views.delFromCart, name='delFromCart'),
]
