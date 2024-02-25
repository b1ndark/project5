from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    """
    This will render the Contact page
    """
    form = ContactForm()
    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)
