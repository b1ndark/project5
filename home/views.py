from django.shortcuts import render
from about.models import About


def index(request):
    """
    This will render the home page
    """

    about = About.objects.first()

    context = {
        'about': about,
    }

    return render(request, 'home/index.html', context)
