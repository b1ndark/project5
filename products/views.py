from django.shortcuts import render


def products(request):
    """ This will render the Products page """
    return render(request, 'products/products.html')
