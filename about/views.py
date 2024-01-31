from django.shortcuts import render


def about(request):
    """
    This will render the About page
    """

    return render(request, 'about/about.html')
