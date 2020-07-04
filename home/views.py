from django.shortcuts import render
from .models import BannerBild, SpielTabelle, NachrichtenLink, Karte, Empfehlung

# Create your views here.
def index(request):
    """ Return home page """
    banner_bild = BannerBild.objects.all()
    spiel_tabelle = SpielTabelle.objects.all()
    news = NachrichtenLink.objects.all()
    karten = Karte.objects.all()
    empfehlungen = Empfehlung.objects.all()

    context = {
        'banner_bild': banner_bild,
        'spiel_tabelle': spiel_tabelle,
        'news': news,
        'karten': karten,
        'empfehlungen': empfehlungen
    }
    return render(request, 'home/index.html', context)