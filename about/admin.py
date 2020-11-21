from django.contrib import admin
from .models import AboutPageBannerPicture, SportsHallInfo, AboutText

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

class AboutTextAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'paragraph1',
        'paragraph2',
        'paragraph3',
        'paragraph4',
        'paragraph5',
        'paragraph6',
        'paragraph7',
        'paragraph8',
        'paragraph9',
        'paragraph10',
    )

admin.site.register(SportsHallInfo, SportsHallInfoAdmin)
admin.site.register(AboutPageBannerPicture, AboutPageBannerPictureAdmin)
admin.site.register(AboutText, AboutTextAdmin)
