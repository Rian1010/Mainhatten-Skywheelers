from django.db import models
from django.db.models import Model

# Create your models here.
class SpielTabelle(models.Model):
    friendly_name = models.CharField(max_length=254, null=False, blank=False)
    home_team = models.CharField(max_length=64, null=False, blank=False)
    away_team = models.CharField(max_length=64, null=False, blank=False)
    venue = models.CharField(max_length=254, null=False, blank=True)
    date = models.DateTimeField(null=False, blank=True)
    result = models.CharField(max_length=16, null=False, blank=True)
    streamlink = models.URLField(max_length=512, null=False, blank=True)

    class Meta:
        verbose_name_plural = "Spieltabelle Reihen"


