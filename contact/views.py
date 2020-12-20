from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ContactInfo
from .forms import ContactInfoForm

# Create your views here.
def contactPage(request):
    """ Return contact page """
    contact_information = ContactInfo.objects.all()

    context = {
        'contact_info': contact_information,
    }

    return render(request, "contact/contact.html", context)


@login_required
def edit_contact_info(request, contact_id):
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('fanshop'))
    contact_info = get_object_or_404(ContactInfo, pk=contact_id)
    if request.method == 'POST':
        form = ContactInfoForm(request.POST, request.FILES, instance=contact_info)
        if form.is_valid():
            form.save()
            messages.success(request, 'Die Information der Kontaktsperson wurde erfolgreich aktualisiert!')
            return redirect(reverse('fanshop'))
        else: 
            messages.error(request, 'Es ist ein Fehler aufgetreten. Bitte stellen Sie sicher, dass das Formular gültig ist.')
    else: 
        form = ContactInfo()
        messages.info(request, f'Sie bearbeiten die Kontaktdaten von "{contact_info.name}"')

    context = {
        'form': form,
        'contact_info': contact_info
    }

    return render(request, 'contact/edit-contact.html', context)
        