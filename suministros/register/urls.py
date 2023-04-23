from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signUp/<str:acceso>/', views.signUp, name='signUp'),
    path('select/', views.seleccionarAcceso, name='select'),
]
