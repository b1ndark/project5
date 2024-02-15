from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_image', 'profile_bio', 'fav_brand',
                  'fav_operating_system', 'default_phone_number',
                  'default_street_address1', 'default_street_address2',
                  'default_town_or_city', 'default_postcode',
                  'default_country', 'default_county',)
