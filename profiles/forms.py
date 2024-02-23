from django import forms
from .widgets import CustomClearableFileInput
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'fav_brand', 'fav_os',
                  'default_phone_number', 'default_street_address1',
                  'default_street_address2', 'default_town_or_city',
                  'default_postcode', 'default_country',
                  'default_county', 'image',)

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'
