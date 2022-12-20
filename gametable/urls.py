from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.gametablePage, name='gametablePage'),
    path('reihe-hinzufügen/', views.add_table_row, name='add_table_row'),
    path('reihe-bearbeiten/<int:table_id>/', views.edit_table_row, name='edit_table_row'),
    path('reihe-löschen/<int:table_id>/', views.delete_table_row, name='delete_table_row')
]