
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/<int:pk>/', views.client_detail, name='client_detail'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:pk>/edit/', views.order_edit, name='order_edit'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),
]
