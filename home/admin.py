from django.contrib import admin
from .models import StartseiteSektion, BannerBild, SpielTabelle, Empfehlung, Karte, NachrichtenLink

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

class NachrichtenLinkAdmin(admin.ModelAdmin):
    list_display = (
        'news_link_titel',
        'link_image',
    )

class KartenAdmin(admin.ModelAdmin):
    list_display = (
        'karten_bild',
        'karten_titel',
        'karten_beschreibung',
        'karten_knopf',
    )

class EmpfehlungAdmin(admin.ModelAdmin):
    list_display = (
        'empfehler_profil_bild',
        'name',
        'okkupation',
        'zitat',
    )

admin.site.register(StartseiteSektion, StartseiteSektionAdmin)
admin.site.register(BannerBild, BannerImageAdmin)
admin.site.register(SpielTabelle, SpielTabelleAdmin)
admin.site.register(NachrichtenLink, NachrichtenLinkAdmin)
admin.site.register(Karte, KartenAdmin)
admin.site.register(Empfehlung, EmpfehlungAdmin)
