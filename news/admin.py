from django.contrib import admin
from .models import NewsHeadlines

# Register your models here.
class NewsHeadlinesAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'heading',
        'time_and_date_published'
    )

admin.site.register(NewsHeadlines, NewsHeadlinesAdmin)