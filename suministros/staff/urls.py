from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='staff'),
    path('detail/<int:id>/', views.detail, name='detailStaff'),
    path('create/', views.create, name='createStaff'),
    path('edit/<int:id>/', views.edit, name='editStaff'),
    path('delete/<int:id>/', views.delete, name='deleteStaff'),
]
