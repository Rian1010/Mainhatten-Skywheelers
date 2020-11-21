from django.shortcuts import render
from .models import SportsHallInfo, AboutPageBannerPicture, AboutText

# Create your views here.
def about_page(request):
    """ Renders About Page """
    table_info = SportsHallInfo.objects.all()
    about_image = AboutPageBannerPicture.objects.all()
    about_text_section = AboutText.objects.all()

    context = {
        'table_info': table_info,
        'banner_image': about_image,
        'about_text_section': about_text_section
    }

    return render(request, 'about/about.html', context)
