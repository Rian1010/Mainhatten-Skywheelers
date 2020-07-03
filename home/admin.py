from django.contrib import admin
from .models import StartseiteSektion, BannerBild, SpielTabelle, Empfehlung, Karte, NewsLink

# Register your models here.

class StartseiteSektionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class BannerImageAdmin(admin.ModelAdmin):
    list_display = (
        'bild',
        'banner_titel',
        'banner_beschreibung',
        'call_to_action_button',
    )
class SpielTabelleAdmin(admin.ModelAdmin):
    list_display = (
        'teams',
        'ort',
        'datum',
    )

admin.site.register(StartseiteSektion, StartseiteSektionAdmin)
admin.site.register(BannerBild, BannerImageAdmin)
admin.site.register(SpielTabelle, SpielTabelleAdmin)
