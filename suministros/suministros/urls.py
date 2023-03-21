from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', include('login.urls')),
    path('product/', include('product.urls')),
    path('supplier/', include('supplier.urls')),
    path('costumer/', include('costumer.urls')),
    path('staff/', include('staff.urls')),
    path('cart/', include('shoppingCart.urls')),
    path('register/', include('register.urls')),
]
