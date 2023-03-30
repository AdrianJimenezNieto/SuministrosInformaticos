from django.urls import path

from . import views

# Cart Urls
urlpatterns = [
    path('', views.index, name='cart'),
    path('list-carts/', views.ListCart.as_view(), name='list-cart'),
    path('<int:pk>/', views.DetailCart.as_view(), name='detail-cart'),
    path('create/', views.CreateCart.as_view(), name='create-cart'),
    path('<int:pk>/update/', views.Updatecart.as_view(), name='update-cart'),
    path('<int:pk>/delete/', views.DeleteCart.as_view(), name='delete-cart'),
    path('cartitem/', views.ListCartItem.as_view(), name='list-cartitem'),
    path('cartitem/<int:pk>/', views.DetailCartItem.as_view(), name='detail-cartitem'),
    path('cartitem/create/', views.CreateItemCart.as_view(), name='create-cartitem'),
    path('cartitem/<int:pk>/update/', views.UpdateCartItem.as_view(), name='update-cartitem'),
    path('cartitem/<int:pk>/delete/', views.DeleteCartItem.as_view(), name='delete-cartitem'),
]

# CartItem Urls
urlpatterns += [
    path('cartitem/', views.ListCartItem.as_view(), name='list-cartitem'),
    path('cartitem/<int:pk>/', views.DetailCartItem.as_view(), name='detail-cartitem'),
    path('cartitem/create/', views.CreateItemCart.as_view(), name='create-cartitem'),
    path('cartitem/<int:pk>/update/', views.UpdateCartItem.as_view(), name='update-cartitem'),
    path('cartitem/<int:pk>/delete/', views.DeleteCartItem.as_view(), name='delete-cartitem'),
]