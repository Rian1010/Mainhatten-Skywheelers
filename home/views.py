from django.shortcuts import render
from .models import BannerBild, SpielTabelle

# Create your views here.
def index(request):
    """ Return home page """
    banner_bild = BannerBild.objects.all()
    spiel_tabelle = SpielTabelle.objects.all()

    context = {
        'banner_bild': banner_bild,
        'spiel_tabelle': spiel_tabelle,
    }
    return render(request, 'home/index.html', context)