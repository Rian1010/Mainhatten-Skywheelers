from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import GameTableForm
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


@login_required
def add_table_row(request):
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('fanshop'))
    if request.method == 'POST':
        form = SpielTabelle(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            messages.success(request, 'Die Spieltabelle wurde erfolgreich hinzugefügt!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Es ist ein Fehler aufgetreten. Bitte stellen Sie sicher, dass das Formular gültig ist.')
    else:
        form = SpielTabelle()
    
    context = {
        'form': form
    }

    return render(request, 'home/add-table-row.html', context)


def edit_table_row(request, table_id):
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('home'))
    table_row = get_object_or_404(SpielTabelle, pk=table_id)
    if request.method == 'POST':
        form = GameTableForm(request.POST, request.FILES, instance=table_row)
        if form.is_valid():
            form.save()
            messages.success(request, 'Die Spieltabelle wurde erfolgreich aktualisiert!')
            return redirect(reverse('home'))
        else: 
            messages.error(request, 'Es ist ein Fehler aufgetreten. Bitte stellen Sie sicher, dass das Formular gültig ist.')
    else: 
        form = GameTableForm(instance=table_row)
        messages.info(request, f'Sie bearbeiten "{table_row.friendly_name}"')

    context = {
        'form': form,
        'table_row': table_row
    }

    return render(request, 'home/edit-table-row.html', context)
        

def delete_table_row(request, table_id):
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('home'))
    table_row = get_object_or_404(SpielTabelle, pk=table_id)
    table_row.delete()
    messages.success(request, 'Die Reihe der Tabelle wurde gelöscht!')
    return redirect(reverse('home'))

