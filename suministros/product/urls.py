from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product'),
    path('detail/<int:id>', views.detail, name='detailProduct'),
    path('create/', views.create, name='createProduct'),
    path('edit/<int:id>', views.edit, name='editProduct'),
    path('delete/<int:id>', views.delete, name='deleteProduct'),
]
