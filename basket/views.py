from django.shortcuts import render


def basket(request):
    """
    This will render the basket page
    """

    return render(request, 'basket/basket.html')
