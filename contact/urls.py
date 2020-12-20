from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.contactPage, name='contactPage'),
    path('bearbeiten/<int:contact_id>', views.edit_contact_info, name='edit_contact_person')
]