from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EventsForm
from .models import EventInfo

# Create your views here.
def events_page(request):
    """ Return Events Page """
    events = EventInfo.objects.all().order_by('start_date')

    context = {
        'events': events
    }

    return render(request, 'events/events.html', context)

def events_content(request, event_id):
    """ Return the Event-Info Page """
    event_info = get_object_or_404(EventInfo, pk=event_id)

    context = {
        "event": event_info
    }

    return render(request, 'events/events-content.html', context)

@login_required
def add_event(request,):
    """ Add an event to the events page """
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('events_page'))

    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES)
        if form.is_valid:
            event_detail = form.save()
            messages.success(request, 'Die Veranstaltung wurde erfolgreich hinzugefügt!')
            return redirect(reverse('events_content', args=[event_detail.id]))
        else:
            messages.error(request, 'Es ist ein Fehler aufgetreten. Bitte stellen Sie sicher, dass das Formular gültig ist.')
    else:
        form = EventsForm()
    
    context = {
        'form': form
    }

    return render(request, 'events/add-event.html', context)

@login_required
def edit_event(request, event_id):
    """ Edit an event from the events page """
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('events_page'))
    event = get_object_or_404(EventInfo, pk=event_id)
    if request.method == 'POST':
        event_form = EventsForm(request.POST, request.FILES, instance=event)
        if event_form.is_valid():
            event_form.save()
            messages.success(request, 'Die Veranstaltung wurde erfolgreich aktualisiert!')
            return redirect(reverse('events_content', args=[event.id]))
        else:
            messages.error(request, 'Es ist ein Fehler aufgetreten. Bitte stellen Sie sicher, dass das Formular gültig ist.')
    else:
        event_form = EventsForm(instance=event)
        messages.info(request, f'Sie bearbeiten "{event.heading}"')
    
    context = {
        'event': event, 
        'form': event_form
    }

    return render(request, 'events/edit-event.html', context)

@login_required
def delete_event(request, event_id):
    """ Delete an event from the events page """
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('eventsPage'))
    event = get_object_or_404(EventInfo, pk=event_id)
    event.delete()
    messages.success(request, 'Die Veranstaltung wurde gelöscht!')
    return redirect(reverse('eventsPage'))