from django import forms
from .models import About


class EditAboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

        widgets = {
            'facebook_url': forms.TextInput(attrs={'placeholder': 'https://facebook.com'}),
            'twitter_url': forms.TextInput(attrs={'placeholder': 'https://twitter.com'}),
            'youtube_url': forms.TextInput(attrs={'placeholder': 'https://youtube.com'}),
            'instagram_url': forms.TextInput(attrs={'placeholder': 'https://instagram.com'}),
        }
