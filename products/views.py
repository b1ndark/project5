from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):
    """ This will render the All Products, will also render all the search and sorting queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ This will render the selected Product and display the information about it """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
