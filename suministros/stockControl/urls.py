from django.urls import path
from . import views

urlpatterns = [
    path('', views.stockControl, name='stockControl'),
]
