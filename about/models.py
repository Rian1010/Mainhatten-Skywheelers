from django.db import models
from django.db.models import Model

# Create your models here.
class AboutPageBannerPicture(models.Model):
    image = models.ImageField(null=False, blank=False)

class SportsHallInfo(models.Model):
    descriptor = models.CharField(max_length=40, null=True, blank=True, default='')
    description = models.CharField(max_length=40, null=True, blank=True, default='')
