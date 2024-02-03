from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def basket(request):
    """
    This will render the basket page
    """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    Add a quantity of a selected product to the basket
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request, f'Updated {product.name}\
             quantity to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(
            request, f'{product.name} has been\
             added to your basket')
    
    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Adjust the quantity of a selected product to the basket
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] = quantity
        messages.success(
            request, f'The quantity of {product.name} has been\
             updated to {basket[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(
            request, f'{product.name} has been\
             removed from your basket')
    
    request.session['basket'] = basket
    return redirect(reverse('basket'))


def remove_from_basket(request, item_id):
    """
    Remove the product from the basket
    """

    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})

        basket.pop(item_id)
        messages.success(
            request, f'{product.name} has been\
             removed from your basket')
            
        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
