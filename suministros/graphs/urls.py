from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.graphs, name='graphs'),
    path('<str:graph>', views.graphs, name='graphs'),
]

