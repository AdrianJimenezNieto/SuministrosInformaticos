from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='supplier'),
    path('detail/', views.detail, name='detailSupplier'),
    path('create/', views.create, name='createSupplier'),
    path('edit/', views.edit, name='editSupplier'),
    path('updatePassword/', views.updatePassword, name='updatePasswordSupplier'),
    path('delete/', views.delete, name='deleteSupplier'),
]
