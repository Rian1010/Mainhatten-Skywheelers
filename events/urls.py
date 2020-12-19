from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_page, name='eventsPage'),
    path('<int:event_id>/', views.events_content, name="events_content"),
    path('hinzufügen/', views.add_event, name="add_event"),
    path('bearbeiten/<int:event_id>/', views.edit_event, name="edit_event"),
    path('löschen/<int:event_id>/', views.delete_event, name="delete_event")
]