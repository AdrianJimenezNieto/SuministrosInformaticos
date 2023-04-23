from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='staff'),
    path('detail/', views.detail, name='detailStaff'),
    #path('create/', views.create, name='createStaff'),
    path('edit/', views.edit, name='editStaff'),
    path('updatePassword/', views.updatePassword, name='updatePasswordStaff'),
    path('delete/', views.delete, name='deleteStaff'),
]
