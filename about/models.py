from django.db import models
from django.core.exceptions import ValidationError


class About(models.Model):
    """
        About model so Admin/Owner can update the about page from admin page
    """

    class Meta:
        verbose_name_plural = 'About Us'

    name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(
        null=True, blank=True, upload_to='about/',
        default='about/no_product_image.webp')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address_1 = models.CharField(max_length=200, null=True, blank=True)
    street_address_2 = models.CharField(max_length=200, null=True, blank=True)
    city_or_town = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    def clean(self):
        if About.objects.exists() and not self.pk:
            raise ValidationError('You can only have one About!')

    def save(self, *args, **kwargs):
        return super(About, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
