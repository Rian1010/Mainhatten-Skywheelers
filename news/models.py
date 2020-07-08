from django.db import models
from django.db.models import Model

# Create your models here.
class NewsHeadlines(models.Model):
    image = models.ImageField(null=False, blank=False)
    heading = models.CharField(max_length=254, null=False, blank=False, default='')
    time_and_date_published = models.DateTimeField(null=False, blank=False, default='')
