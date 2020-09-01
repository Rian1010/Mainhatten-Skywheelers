from django.shortcuts import render
from .models import ContactInfo

# Create your views here.
def contactPage(request):
    """ Return contact page """
    contact_information = ContactInfo.objects.all()

    context = {
        'contact_info': contact_information,
    }

    return render(request, "contact/contact.html", context)