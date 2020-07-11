from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_page , name='news_page'),
    path('<int:article_id>/', views.article_content, name="article_content")
]
