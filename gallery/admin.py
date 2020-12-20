from django.contrib import admin
from .models import mainGalleryPage, firstGalleryPictures, secondGalleryPictures, thirdGalleryPictures, firstGalleryPageTitle, secondGalleryPageTitle, thirdGalleryPageTitle
 
# Register your models here.
class mainGalleryPageAdmin(admin.ModelAdmin):
    list_display = (
        'page_title',
        'image1',
        'heading1',
        'image2',
        'heading2',
        'image3',
        'heading3',
    )

class firstGalleryPageTitleAdmin(admin.ModelAdmin):
    list_display = (
        'page_image',
        'page_title',
    )

class firstGalleryPageAdmin(admin.ModelAdmin):
    list_display = (
        'image_column_1',
        'image_column_2',
        'image_column_3',
        'image_column_4',
    )

class secondGalleryPageTitleAdmin(admin.ModelAdmin):
    list_display = (
        'page_image',
        'page_title',
    )

class secondGalleryPageAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'image_column_1',
        'image_column_2',
        'image_column_3',
        'image_column_4',
    )

class thirdGalleryPageTitleAdmin(admin.ModelAdmin):
    list_display = (
        'page_image',
        'page_title',
    )

class thirdGalleryPageAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'image_column_1',
        'image_column_2',
        'image_column_3',
        'image_column_4',
    )

admin.site.register(mainGalleryPage, mainGalleryPageAdmin)
admin.site.register(firstGalleryPageTitle, firstGalleryPageTitleAdmin)
admin.site.register(firstGalleryPictures, firstGalleryPageAdmin)
admin.site.register(secondGalleryPageTitle, secondGalleryPageTitleAdmin)
admin.site.register(secondGalleryPictures, secondGalleryPageAdmin)
admin.site.register(thirdGalleryPageTitle, thirdGalleryPageTitleAdmin)
admin.site.register(thirdGalleryPictures, thirdGalleryPageAdmin)
