from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainGalleryPageView, name="main_gallery"),
    path('erste-gallerie/', views.firstGalleryPageView, name="first_gallery"),
    path('erste-gallerie/hinzufügen/', views.addImgFirstGallery, name="add_img_first_gallery"),
    path('erste-gallerie/löschen/<int:picture_id>/', views.deleteImgFirstGallery, name="delete_img_first_gallery"),
    path('erste-gallerie/bearbeiten/<int:picture_id>/', views.editImgFirstGallery, name="edit_img_first_gallery"),
    path('zweite-gallerie/', views.secondGalleryPageView, name="second_gallery"),
    path('zweite-gallerie/hinzufügen/', views.addImgSecondGallery, name="add_img_second_gallery"),
    path('zweite-gallerie/löschen/<int:picture_id>/', views.deleteImgSecondGallery, name="delete_img_second_gallery"),
    path('zweite-gallerie/bearbeiten/<int:picture_id>/', views.editImgSecondGallery, name="edit_img_second_gallery"),
    path('dritte-gallerie/', views.thirdGalleryPageView, name="third_gallery"),
    path('dritte-gallerie/hinzufügen/', views.addImgThirdGallery, name="add_img_third_gallery"),
    path('dritte-gallerie/löschen/<int:picture_id>/', views.deleteImgThirdGallery, name="delete_img_third_gallery"),
    path('dritte-gallerie/bearbeiten/<int:picture_id>/', views.editImgThirdGallery, name="edit_img_third_gallery"),
]