from django.contrib import admin
from .models import Product, BannerImage

# Register your models here.
class BannerImageAdmin(admin.ModelAdmin):
    list_display = [
        'page_title',
        'banner'
    ]

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'image',
        'name',
        'description',
        'price'
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(BannerImage, BannerImageAdmin)