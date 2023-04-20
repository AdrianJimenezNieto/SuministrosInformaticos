from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='supplier'),
    path('detail/<int:id>/', views.detail, name='detailSupplier'),
    path('create/', views.create, name='createSupplier'),
    path('edit/<int:id>/', views.edit, name='editSupplier'),
    path('updatePassword/<int:id>/', views.updatePassword, name='updatePasswordSupplier'),
    path('delete/<int:id>/', views.delete, name='deleteSupplier'),
]
