from django.shortcuts import render, redirect, reverse, HttpResponse


def basket(request):
    """
    This will render the basket page
    """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    Add a quantity of a selected product to the basket
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
    
    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Adjust the quantity of a selected product to the basket
    """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] = quantity
    else:
        basket.pop(item_id)
    
    request.session['basket'] = basket
    return redirect(reverse('basket'))


def remove_from_basket(request, item_id):
    """
    Remove the product from the basket
    """

    try:
        basket = request.session.get('basket', {})

        basket.pop(item_id)
            
        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
