from django.contrib import admin
from .models import ContactInfo

# Register your models here.
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = (
        'contactHeading',
        'name',
        'image',
        'addressLine1',
        'addressLine2',
        'addressLine3',
        'addressLine4',
        'phoneHeading',
        'phoneNumber',
        'emailHeading',
        'email',
    )

admin.site.register(ContactInfo, ContactInfoAdmin)