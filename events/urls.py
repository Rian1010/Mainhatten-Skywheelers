from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_page, name='eventsPage'),
    path('<int:event_id>', views.events_content, name="events_content")
]