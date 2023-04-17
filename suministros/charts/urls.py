from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.chart, name='charts'),
    path('<int:user_id><str:chartType>/', views.chart, name='charts'),
]
 