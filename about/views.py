from django.shortcuts import render, get_object_or_404
from .models import About


def about(request, about_id):
    """ This will render the About page """

    about = get_object_or_404(About, pk=about_id)
    
    context = {
        'about': about,
    }

    return render(request, 'about/about.html', context)
