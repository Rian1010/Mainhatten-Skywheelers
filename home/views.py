from django.shortcuts import render
from .models import BannerBild, SpielTabelle, NachrichtenLink, Karte, Empfehlung, Sponsor, CallToActionSektion

# Create your views here.
def index(request):
    """ Return home page """
    banner_bild = BannerBild.objects.all()
    sponsor = Sponsor.objects.all()
    spiel_tabelle = SpielTabelle.objects.all()
    news = NachrichtenLink.objects.all()
    karten = Karte.objects.all()
    call_to_action = CallToActionSektion.objects.all()

    empfehlungen = Empfehlung.objects.all()
    erste_empfehlung = empfehlungen[0]
    zweite_empfehlung = empfehlungen[1]


    context = {
        'banner_bild': banner_bild,
        'sponsor': sponsor,
        'spiel_tabelle': spiel_tabelle,
        'news': news,
        'karten': karten,
        'erste_empfehlung': erste_empfehlung,
        'zweite_empfehlung': zweite_empfehlung,
        'call_to_action': call_to_action
    }
    return render(request, 'home/index.html', context)