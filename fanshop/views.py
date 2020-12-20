from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, BannerImage
from .forms import ProductForm


# Create your views here.
def fanshop_page(request):
    """ Return fanshop page """
    banner = BannerImage.objects.all()
    products = Product.objects.all()

    context = {
        'banner': banner,
        'products': products
    }

    return render(request, 'fanshop/fanshop.html', context)


@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('fanshop'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            messages.success(request,  'Das Produkt wurden erfolgreich hinzugefügt!')
            return redirect(reverse('fanshop'))
        else:
            messages.error(request, 'Es ist ein Fehler aufgetreten. Bitte stellen Sie sicher, dass das Formular gültig ist.')
    else:
        form = ProductForm()
    
    context = {
        'form': form
    }

    return render(request, 'fanshop/add-product.html', context)


def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('fanshop'))
    product_item = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Das Produkt wurde erfolgreich aktualisiert!')
            return redirect(reverse('fanshop'))
        else: 
            messages.error(request, 'Es ist ein Fehler aufgetreten. Bitte stellen Sie sicher, dass das Formular gültig ist.')
    else: 
        form = ProductForm(instance=product_item)
        messages.info(request, f'Sie bearbeiten "{product_item.friendly_name}"')

    context = {
        'form': form,
        'product_item': product_item
    }

    return render(request, 'fanshop/edit-product.html', context)
        

def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Verzeihung! Nur Besitzer dieser Website können das machen.")
        return redirect(reverse('fanshop'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Die Produkt wurde gelöscht!')
    return redirect(reverse('fanshop'))

