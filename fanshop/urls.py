from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fanshop_page, name='fanshop'),
    path('hinzufügen/', views.add_product, name='add_product'),
    path('bearbeiten/<int:product_id>/', views.edit_product, name='edit_product'),
    path('löschen/<int:product_id>/', views.delete_product, name='delete_product')
]