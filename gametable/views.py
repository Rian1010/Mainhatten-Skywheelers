from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import GameTableForm
from .models import SpielTabelle

from datetime import date

# Create your views here.
def gametablePage(request):
    """ Render Game Table Page """

    today = date.today()

    gametable = SpielTabelle.objects.all()#.order_by('date')
    upcoming = list(gametable.filter(date__gte=today).order_by('date'))
    results =   list(gametable.filter(date__lt=today).order_by('-date'))

    #list(gametable.filter(date=today)) +

    context = {
        'gametable': upcoming,
        'results': results
    }
    return render(request, 'gametable/gametable.html', context)

@login_required
def add_table_row(request):
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('gametablePage'))
    if request.method == 'POST':
        form = GameTableForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            messages.success(request, 'Die Spieltabelle wurde erfolgreich hinzugefügt!')
            return redirect(reverse('gametablePage'))
        else:
            messages.error(request, 'Es ist ein Fehler aufgetreten. Bitte stellen Sie sicher, dass das Formular gültig ist.')
    else:
        form = GameTableForm()
    
    context = {
        'form': form
    }

    return render(request, 'gametable/add-table-row.html', context)

def edit_table_row(request, table_id):
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('gametablePage'))
    table_row = get_object_or_404(SpielTabelle, pk=table_id)
    if request.method == 'POST':
        form = GameTableForm(request.POST, request.FILES, instance=table_row)
        if form.is_valid():
            form.save()
            messages.success(request, 'Die Spieltabelle wurde erfolgreich aktualisiert!')
            return redirect(reverse('gametablePage'))
        else: 
            messages.error(request, 'Es ist ein Fehler aufgetreten. Bitte stellen Sie sicher, dass das Formular gültig ist.')
    else: 
        form = GameTableForm(instance=table_row)
        messages.info(request, f'Sie bearbeiten "{table_row.friendly_name}"')

    context = {
        'form': form,
        'table_row': table_row
    }

    return render(request, 'gametable/edit-table-row.html', context)
        

def delete_table_row(request, table_id):
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('gametablePage'))
    table_row = get_object_or_404(SpielTabelle, pk=table_id)
    table_row.delete()
    messages.success(request, 'Die Reihe der Tabelle wurde gelöscht!')
    return redirect(reverse('gametablePage'))