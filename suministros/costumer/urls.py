from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='costumer'),
    path('detail/', views.detail, name='detailCostumer'),
    path('create/', views.create, name='createCostumer'),
    path('edit/', views.edit, name='editCostumer'),
    path('updatePassword/', views.updatePassword, name='updatePasswordCostumer'),
    path('delete/', views.delete, name='deleteCostumer'),
]
