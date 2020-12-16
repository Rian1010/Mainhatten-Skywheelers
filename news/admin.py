from django.contrib import admin
from .models import NewsHeadline

# Register your models here.
class NewsHeadlineAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'heading',
        'second_heading',
        'time_and_date_published',
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
        'friendly_name',
    )

admin.site.register(NewsHeadline, NewsHeadlineAdmin)