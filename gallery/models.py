from django.db import models
from django.db.models import Model

# Create your models here.
class mainGalleryPage(models.Model):
    page_title = models.CharField(max_length=254, null=False, blank=False, default='')
    image1 = models.ImageField(null='False', blank='False')
    heading1 = models.CharField(max_length=100, null=False, blank=False, default='')
    image2 = models.ImageField(null='False', blank='False')
    heading2 = models.CharField(max_length=100, null=False, blank=False, default='')
    image3 = models.ImageField(null='False', blank='False')
    heading3 = models.CharField(max_length=100, null=False, blank=False, default='')

class firstGalleryPageTitle(models.Model):
    page_title = models.CharField(max_length=254, null=False, blank=False, default='')

class firstGalleryPictures(models.Model):
    image_column_1 = models.ImageField(null=True, blank=True)
    image_column_2 = models.ImageField(null=True, blank=True)
    image_column_3 = models.ImageField(null=True, blank=True)
    image_column_4 = models.ImageField(null=True, blank=True)

class secondGalleryPageTitle(models.Model):
    page_title = models.CharField(max_length=254, null=False, blank=False, default='')

class secondGalleryPictures(models.Model):
    image_column_1 = models.ImageField(null=True, blank=True)
    image_column_2 = models.ImageField(null=True, blank=True)
    image_column_3 = models.ImageField(null=True, blank=True)
    image_column_4 = models.ImageField(null=True, blank=True)

class thirdGalleryPageTitle(models.Model):
    page_title = models.CharField(max_length=254, null=False, blank=False, default='')

class thirdGalleryPictures(models.Model):
    image_column_1 = models.ImageField(null=True, blank=True)
    image_column_2 = models.ImageField(null=True, blank=True)
    image_column_3 = models.ImageField(null=True, blank=True)
    image_column_4 = models.ImageField(null=True, blank=True)
