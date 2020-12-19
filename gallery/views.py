from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import mainGalleryPage, firstGalleryPictures, secondGalleryPictures, thirdGalleryPictures, firstGalleryPageTitle, secondGalleryPageTitle, thirdGalleryPageTitle
from .forms import firstGalleryImgForm, firstGalleryTitleForm

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

def addImgFirstGallery(request):
    """ Add images to the first gallery """
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('first_gallery'))
    if request.method == 'POST':
        form = firstGalleryImgForm(request.POST, request.FILES)
        if form.is_valid:
            gallery_img = form.save()
            messages.success(request, 'Das Bild wurde erfolgreich hinzugefügt!')
            return redirect(reverse('first_gallery'))
        else:
            messages.error(request, 'Es ist ein Fehler aufgetreten. Bitte stellen Sie sicher, dass das Formular gültig ist.')
    else:
        form = firstGalleryImgForm()

    context = {
        'form': form
    }

    return render(request, 'gallery/add-img-first-gallery.html', context)


def editImgFirstGallery(request, picture_id):
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('first_gallery'))
    image_row = get_object_or_404(firstGalleryPictures, pk=picture_id)
    if request.method == 'POST':
        form = firstGalleryImgForm(request.POST, request.FILES, instance=image_row)
        if form.is_valid():
            form.save()
            messages.success(request, 'Die Pressemitteilung wurde erfolgreich aktualisiert!')
            return redirect(reverse('first_gallery'))
        else: 
            messages.error(request, 'Es ist ein Fehler aufgetreten. Bitte stellen Sie sicher, dass das Formular gültig ist.')
    else: 
        form = firstGalleryImgForm(instance=image_row)
        messages.info(request, f'Sie bearbeiten "{image_row.friendly_name}"')

    context = {
        'form': form,
        'gallery_row': image_row
    }

    return render(request, 'gallery/edit-img-first-gallery.html', context)
        

def deleteImgFirstGallery(request, picture_id):
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('first_gallery'))
    picture = get_object_or_404(firstGalleryPictures, pk=picture_id)
    picture.delete()
    messages.success(request, 'Die Reihe wurde gelöscht!')
    return redirect(reverse('first_gallery'))


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
