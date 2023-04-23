from django.urls import path
from . import views

urlpatterns = [
    path('', views.stockControl, name='stockControl'),
    path('buy/<int:stockControl_id>/', views.buyStock, name='buyStock'),
]
