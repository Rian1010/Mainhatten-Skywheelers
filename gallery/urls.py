from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainGalleryPageView, name="main_gallery"),
    path('ingskywheelers1/', views.firstGalleryPageView, name="first_gallery"),
    path('ingskywheelers1/hinzufügen/', views.addImgFirstGallery, name="add_img_first_gallery"),
    path('ingskywheelers1/löschen/<int:picture_id>/', views.deleteImgFirstGallery, name="delete_img_first_gallery"),
    path('ingskywheelers1/bearbeiten/<int:picture_id>/', views.editImgFirstGallery, name="edit_img_first_gallery"),
    path('ingskywheelers2/', views.secondGalleryPageView, name="second_gallery"),
    path('ingskywheelers2/hinzufügen/', views.addImgSecondGallery, name="add_img_second_gallery"),
    path('ingskywheelers2/löschen/<int:picture_id>/', views.deleteImgSecondGallery, name="delete_img_second_gallery"),
    path('ingskywheelers2/bearbeiten/<int:picture_id>/', views.editImgSecondGallery, name="edit_img_second_gallery"),
    path('bilder/', views.thirdGalleryPageView, name="third_gallery"),
    path('bilder/hinzufügen/', views.addImgThirdGallery, name="add_img_third_gallery"),
    path('bilder/löschen/<int:picture_id>/', views.deleteImgThirdGallery, name="delete_img_third_gallery"),
    path('bilder/bearbeiten/<int:picture_id>/', views.editImgThirdGallery, name="edit_img_third_gallery"),
]