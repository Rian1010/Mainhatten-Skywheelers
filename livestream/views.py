from django.shortcuts import render

# Create your views here.
def stream_page(request):
    """ Renders Live Stream Page """
    return render(request, 'live_stream/stream.html')