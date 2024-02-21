from django import forms
from .widgets import CustomClearableFileInput
from .models import About


class EditAboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

        widgets = {
            'facebook_url': forms.TextInput(
                attrs={'placeholder': 'https://facebook.com'}),
            'twitter_url': forms.TextInput(
                attrs={'placeholder': 'https://twitter.com'}),
            'youtube_url': forms.TextInput(
                attrs={'placeholder': 'https://youtube.com'}),
            'instagram_url': forms.TextInput(
                attrs={'placeholder': 'https://instagram.com'}),
        }

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'
