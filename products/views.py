from django.shortcuts import render, get_object_or_404
from .models import Product
from django.conf import settings


MEDIA_URL = settings.MEDIA_URL

# Create your views here.
def all_products(request):
    """ A view for product app """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_details(request, product_id):
    """ A view for product details - shows the details of selected product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_details.html', context)