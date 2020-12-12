from django.shortcuts import render

# Create your views here.
def events_page(request):
    """Return Events Page"""
    return render(request, 'events/events.html')