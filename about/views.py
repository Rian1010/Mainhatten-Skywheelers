from django.shortcuts import render
from .models import SportsHallInfo

# Create your views here.
def about_page(request):
    """ Renders About Page """
    table_info = SportsHallInfo.objects.all()
    about_image = AboutPageBannerPicture.objects.all()

    context = {
        'table_info': table_info,
        'image': about_image
    }

    return render(request, 'about/about.html', context)
