from django.shortcuts import render
from .models import Product


def products(request):
    """ This will render the All Products, will also render all the search and sorting queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
