from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cart'),
    path('add/<int:id>', views.add, name='cartAddItem'),
    path('delete/<int:id>', views.delete, name='cartDeleteItem'),
]
