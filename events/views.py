from django.shortcuts import render, get_object_or_404
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
        "event_infos": event_info
    }

    return render(request, 'events/events-content.html', context)
