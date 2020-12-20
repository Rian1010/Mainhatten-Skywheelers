from django.db import models
from django.db.models import Model

# Create your models here.
class BannerImage(models.Model):
    page_title = models.CharField(max_length=100, null=False, blank=False, default='')
    banner = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.page_title

class Product(models.Model):
    friendly_name = models.CharField(max_length=254, null=False, blank=False, default='')
    name = models.CharField(max_length=254, null=False, blank=False, default='')
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name