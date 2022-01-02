from django.urls import path
from . import views

urlpatterns = [
    path('stuff_board/', views.staff_board, name='stuff_board'),
    path('order_board/', views.order_board, name='order_board'),
    path('order_detail/<int:pk>', views.complete_order, name='order_detail'),
    path('order_completed', views.completed_order_view, name='completed_order_view'),
    path('order_list_view/', views.order_list_view, name='order_list_view')
]