from django.shortcuts import render


def contact(request):
    """
    This will render the Contact page
    """

    return render(request, 'contact/contact.html')
