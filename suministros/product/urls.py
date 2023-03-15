from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product'),
    path('create', views.create, name='create'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
]
