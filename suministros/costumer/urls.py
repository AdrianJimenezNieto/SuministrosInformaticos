from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='costumer'),
    path('detail/<int:id>/', views.detail, name='detailCostumer'),
    path('create/', views.create, name='createCostumer'),
    path('edit/<int:id>/', views.edit, name='editCostumer'),
    path('updatePassword/<int:id>/', views.updatePassword, name='updatePasswordCostumer'),
    path('delete/<int:id>/', views.delete, name='deleteCostumer'),
]
