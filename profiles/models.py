from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import BRANDS, OS
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User Profile, so user can maintain profile,
    delete account, delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/',
        default='profiles/default_profile.png')
    profile_bio = models.TextField(verbose_name='Biography',
        null=True, blank=True)
    fav_brand = models.CharField(verbose_name='Favourite Brand',
        max_length=30, choices=BRANDS, null=True, blank=True, default='')
    fav_operating_system = models.CharField(
        verbose_name='Favourite Operating System',
        max_length=30, choices=OS, null=True, blank=True, default='')
    default_phone_number = models.CharField(verbose_name='Phone Number',
        max_length=20, null=True, blank=True)
    default_country = CountryField(verbose_name='Country',
        blank_label='Select Country', null=True, blank=True)
    default_postcode = models.CharField(verbose_name='Postal Code',
        max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(verbose_name='Town or City',
        max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(verbose_name='Street Address',
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(verbose_name='Street Address 2',
        max_length=80, null=True, blank=True)
    default_county = models.CharField(verbose_name='County',
        max_length=40, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create/Update User profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
