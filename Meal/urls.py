from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_menu, name='food_menu'),
    path('food_detail/<int:pk>', views.food_detail, name='food_detail'),
    path('order_complete/<int:pk>', views.order_complete, name='order_complete')
]