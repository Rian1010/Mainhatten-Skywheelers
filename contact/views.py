from django.shortcuts import render

# Create your views here.
def contactPage(request):
    """ Return contact page """
    return render(request, "contact/contact.html")