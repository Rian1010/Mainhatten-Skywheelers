from django.shortcuts import render
from .models import mainGalleryPage, firstGalleryPictures, secondGalleryPictures, thirdGalleryPictures, firstGalleryPageTitle, secondGalleryPageTitle, thirdGalleryPageTitle

# Create your views here.
def mainGalleryPageView(request):
    """ Returns the main gallery page """
    main_gallery = mainGalleryPage.objects.all()

    context = {
        'main_gallery': main_gallery,
    }

    return render(request, 'gallery/main-gallery.html', context)


def firstGalleryPageView(request):
    """ Returns the first gallery page """
    page_title = firstGalleryPageTitle.objects.all()
    first_gallery_pic = firstGalleryPictures.objects.all()

    context = {
        'gallery1_page_title': page_title,
        'first_gallery_pic': first_gallery_pic,
    }

    return render(request, 'gallery/gallery-1.html', context)


def secondGalleryPageView(request):
    """ Returns the first gallery page """
    page_title = secondGalleryPageTitle.objects.all()
    second_gallery_pic = secondGalleryPictures.objects.all()

    context = {
        'gallery2_page_title': page_title,
        'second_gallery_pic': second_gallery_pic,
    }

    return render(request, 'gallery/gallery-2.html', context)


def thirdGalleryPageView(request):
    """ Returns the first gallery page """
    page_title = thirdGalleryPageTitle.objects.all()
    third_gallery_pic = thirdGalleryPictures.objects.all()

    context = {
        'gallery3_page_title': page_title,
        'third_gallery_pic': third_gallery_pic,
    }

    return render(request, 'gallery/gallery-3.html', context)
