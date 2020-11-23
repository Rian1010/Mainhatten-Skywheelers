from django.shortcuts import render
from .models import Product, BannerImage

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