from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainGalleryPageView, name="main_gallery"),
    path('erste-gallerie/', views.firstGalleryPageView, name="first_gallery"),
    path('zweite-gallerie/', views.secondGalleryPageView, name="second_gallery"),
    path('dritte-gallerie/', views.thirdGalleryPageView, name="third_gallery"),
]