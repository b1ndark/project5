from django.shortcuts import render
from about.models import About


def basket(request):
    """
    This will render the basket page
    """

    about = About.objects.first()

    context = {
        'about': about,
    }
    return render(request, 'basket/basket.html', context)
