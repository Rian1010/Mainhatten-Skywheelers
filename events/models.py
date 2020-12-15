from django.db import models
from django.db.models import Model

# Create your models here.
class EventInfo(models.Model):
    heading = models.CharField(max_length=254, null=False, blank=False, default='')
    short_description = models.CharField(max_length=254, null=False, blank=False, default='')
    image = models.ImageField(null=True, blank=True, default='')
    start_date = models.DateTimeField(blank=False,  default=None)
    end_date = models.DateTimeField(blank=False,  default=None)
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

    verbose_name_plural = 'Events'

    def __str__(self):
        return self.heading

