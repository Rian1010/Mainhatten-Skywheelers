from django.shortcuts import render

# Create your views here.
def gametablePage(request):
    """ Render Game Table Page """
    return render(request, 'gametable/gametable.html')