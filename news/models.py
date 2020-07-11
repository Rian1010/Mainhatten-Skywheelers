from django.db import models
from django.db.models import Model

# Create your models here.
class NewsHeadlines(models.Model):
    image = models.ImageField(null=False, blank=False)
    heading = models.CharField(max_length=254, null=False, blank=False, default='')
    second_heading = models.CharField(max_length=254, null=True, blank=True, default='')
    time_and_date_published = models.DateTimeField(null=False, blank=False, default='')
    paragraph1 = models.TextField(default='')
    paragraph2 = models.TextField(default='')
    paragraph3 = models.TextField(default='')
    paragraph4 = models.TextField(default='')
    paragraph5 = models.TextField(default='')
    paragraph6 = models.TextField(default='')
    paragraph7 = models.TextField(default='')
    paragraph8 = models.TextField(default='')
    paragraph9 = models.TextField(default='')
    paragraph10 = models.TextField(default='')
