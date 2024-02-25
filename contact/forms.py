from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    To render a contact form
    """

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]
