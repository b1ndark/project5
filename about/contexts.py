from .models import About


def about_contents(request):
    """
    To render the about info in every page footer
    """

    about = About.objects.first()

    context = {
        'about': about,
    }

    return context
