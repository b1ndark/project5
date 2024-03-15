from django.db import models
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError


class About(models.Model):
    """
    About model so Admin/Owner can update
    the about page and footer from admin page or
    Account menu if Admin is logged in
    """

    class Meta:
        verbose_name_plural = 'Company'

    name = models.CharField(max_length=200)
    email_address = models.EmailField(null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(
        null=True, blank=True, upload_to='about/',
        default='default_images/no_image.webp')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address_1 = models.CharField(
        max_length=200, null=True, blank=True)
    street_address_2 = models.CharField(
        max_length=200, null=True, blank=True)
    city_or_town = models.CharField(max_length=100, null=True, blank=True)
    country = CountryField(blank_label='Select Country', null=True, blank=True)
    postcode = models.CharField(max_length=100, null=True, blank=True)
    opening_hours_mon_to_fri = models.CharField(
        max_length=100, null=True, blank=True)
    opening_hours_sat = models.CharField(
        max_length=100, null=True, blank=True)
    opening_hours_sunday = models.CharField(
        max_length=100, null=True, blank=True)
    opening_hours_bank_holidays = models.CharField(
        max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    facebook_url = models.CharField(max_length=200, null=True, blank=True)
    twitter_url = models.CharField(max_length=200, null=True, blank=True)
    youtube_url = models.CharField(max_length=200, null=True, blank=True)
    instagram_url = models.CharField(max_length=200, null=True, blank=True)

    def clean(self):
        if About.objects.exists() and not self.pk:
            raise ValidationError('You can only have one About!')

    def save(self, *args, **kwargs):
        return super(About, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
