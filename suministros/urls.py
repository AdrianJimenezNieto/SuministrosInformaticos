from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('product/', include('product.urls')),
    path('supplier/', include('supplier.urls')),
    path('costumer/', include('costumer.urls')),
    path('staff/', include('staff.urls')),
    path('register/', include('register.urls')),
    path('sales/', include('sale.urls')),
    path('cart/', include('cart.urls')),
    path('stockContol/', include('stockControl.urls')),
    path('charts/', include('charts.urls')),
]
