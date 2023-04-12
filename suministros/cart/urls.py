from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.viewCart, name='cart'),
    path('add/<int:product_id><int:user_id>/', views.addToCart, name='addToCart'),
    path('delete/<int:item_id><int:user_id>/', views.delFromCart, name='delFromCart'),
]
