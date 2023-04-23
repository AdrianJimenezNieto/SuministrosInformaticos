from django.urls import path
from . import views

urlpatterns = [
    path('', views.chart, name='charts'),
    path('<str:chartType>/', views.chart, name='charts'),
]
 