from django.contrib import admin
from .models import AboutPageBannerPicture, SportsHallInfo

# Register your models here.
class AboutPageBannerPictureAdmin(admin.ModelAdmin):
    list_display = (
        'image',
    )

class SportsHallInfoAdmin(admin.ModelAdmin):
    list_display = (
        'descriptor',
        'description',
    )

admin.site.register(SportsHallInfo, SportsHallInfoAdmin)
admin.site.register(AboutPageBannerPicture, AboutPageBannerPictureAdmin)
