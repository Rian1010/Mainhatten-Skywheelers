from django.db import models
from django.db.models import Model

class ContactInfo(models.Model):
    contactHeading = models.CharField(max_length=100, null=False, blank=False, default='')
    name = models.CharField(max_length=100, null=False, blank=False, default='')
    image = models.ImageField(null=False, blank=False)
    addressLine1 = models.CharField(max_length=100, null=True, blank=True, default='')
    addressLine2 = models.CharField(max_length=100, null=True, blank=True, default='')
    addressLine3 = models.CharField(max_length=100, null=True, blank=True, default='')
    addressLine4 = models.CharField(max_length=100, null=True, blank=True, default='')
    phoneHeading = models.CharField(max_length=40, null=True, blank=True, default='')
    phoneNumber =  models.CharField(max_length=20, null=True, blank=True, default='')
    emailHeading = models.CharField(max_length=20, null=True, blank=True, default='')
    email = models.EmailField(max_length=100, null=True, blank=True, default='')
