from django.db import models
from django.db.models import Model

# Create your models here.
class AboutPageBannerPicture(models.Model):
    image = models.ImageField(null=False, blank=False)

class SportsHallInfo(models.Model):
    descriptor = models.CharField(max_length=40, null=True, blank=True, default='')
    description = models.CharField(max_length=40, null=True, blank=True, default='')

class AboutText(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False, default='')
    paragraph1 = models.TextField(default='', null=False, blank=False)
    paragraph2 = models.TextField(default='', null=True, blank=True)
    paragraph3 = models.TextField(default='', null=True, blank=True)
    paragraph4 = models.TextField(default='', null=True, blank=True)
    paragraph5 = models.TextField(default='', null=True, blank=True)
    paragraph6 = models.TextField(default='', null=True, blank=True)
    paragraph7 = models.TextField(default='', null=True, blank=True)
    paragraph8 = models.TextField(default='', null=True, blank=True)
    paragraph9 = models.TextField(default='', null=True, blank=True)
    paragraph10 = models.TextField(default='', null=True, blank=True)
