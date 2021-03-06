from django.db import models
from django.db.models import Model

# Create your models here.
class mainGalleryPage(models.Model):
    page_title = models.CharField(max_length=254, null=False, blank=False, default='')
    image1 = models.ImageField(null=False, blank=False, default='')
    heading1 = models.CharField(max_length=100, null=False, blank=False, default='')
    image2 = models.ImageField(null=False, blank=False, default='')
    heading2 = models.CharField(max_length=100, null=False, blank=False, default='')
    image3 = models.ImageField(null=False, blank=False, default='')
    heading3 = models.CharField(max_length=100, null=False, blank=False, default='')

class firstGalleryPageTitle(models.Model):
    page_image = models.ImageField(null=False, blank=False, default='')
    page_title = models.CharField(max_length=254, null=False, blank=False, default='')

class firstGalleryPictures(models.Model):
    friendly_name = models.CharField(max_length=254, null=False, blank=False, default='')
    image_column_1 = models.ImageField(null=True, blank=True, default='')
    image_column_2 = models.ImageField(null=True, blank=True, default='')
    image_column_3 = models.ImageField(null=True, blank=True, default='')
    image_column_4 = models.ImageField(null=True, blank=True, default='')

class secondGalleryPageTitle(models.Model):
    page_image = models.ImageField(null=False, blank=False, default='')
    page_title = models.CharField(max_length=254, null=False, blank=False, default='')

class secondGalleryPictures(models.Model):
    friendly_name = models.CharField(max_length=254, null=False, blank=False, default='')
    image_column_1 = models.ImageField(null=True, blank=True, default='')
    image_column_2 = models.ImageField(null=True, blank=True, default='')
    image_column_3 = models.ImageField(null=True, blank=True, default='')
    image_column_4 = models.ImageField(null=True, blank=True, default='')

class thirdGalleryPageTitle(models.Model):
    page_image = models.ImageField(null=False, blank=False, default='')
    page_title = models.CharField(max_length=254, null=False, blank=False, default='')

class thirdGalleryPictures(models.Model):
    friendly_name = models.CharField(max_length=254, null=False, blank=False, default='')
    image_column_1 = models.ImageField(null=True, blank=True, default='')
    image_column_2 = models.ImageField(null=True, blank=True, default='')
    image_column_3 = models.ImageField(null=True, blank=True, default='')
    image_column_4 = models.ImageField(null=True, blank=True, default='')
