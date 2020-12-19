from django.db import models
from django.db.models import Model

# Create your models here.
class NewsHeadline(models.Model):
    friendly_name = models.CharField(max_length=254, null=False, blank=False, default='')
    image = models.ImageField(null=True, blank=True)
    heading = models.CharField(max_length=254, null=False, blank=False, default='')
    second_heading = models.CharField(max_length=254, null=True, blank=True, default='')
    time_and_date_published = models.DateTimeField(null=False, blank=False, default='')
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

    verbose_name_plural = 'Pressemitteilungen'

    def get_friendly_name(self):
        return self.friendly_name
