from django.contrib import admin
from .models import EventInfo

# Register your models here.
class EventInfoAdmin(admin.ModelAdmin):
    list_display = (
        'heading',
        'short_description',
        'image',
        'start_date',
        'end_date',
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

admin.site.register(EventInfo, EventInfoAdmin)