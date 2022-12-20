from django.contrib import admin
from .models import SpielTabelle

# Register your models here.
class SpielTabelleAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'home_team',
        'away_team',
        'venue',
        'date',
        'result',
        'streamlink',
    )

    ordering = ['date']

admin.site.register(SpielTabelle, SpielTabelleAdmin)