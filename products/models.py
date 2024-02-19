from django.db import models

"""
List of operating systems
"""
OS = (
    ('android', 'Android'),
    ('ios', 'iOS'),
    ('linux', 'Linux'),
    ('windows', 'Windows'),
    ('macos', 'macOS'),
)

"""
List of Makers/Brands
"""
BRANDS = (
    ('acer', 'Acer'),
    ('apple', 'Apple'),
    ('asus', 'Asus'),
    ('dell', 'Dell'),
    ('google', 'Google'),
    ('hp', 'HP'),
    ('msi', 'MSI'),
    ('toshiba', 'Toshiba'),
    ('sony', 'Sony'),
)


class Category(models.Model):
    """ Products categories """
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Products """
    name = models.CharField(max_length=200)
    image = models.ImageField(
        null=True, blank=True, upload_to='products/',
        default='default_images/no_image.webp')
    description = models.TextField()
    brand = models.CharField(
        max_length=30, choices=BRANDS, null=True, blank=True, default='')
    operating_system = models.CharField(
        max_length=30, choices=OS, null=True, blank=True, default='')
    sku = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    memory_ram = models.CharField(max_length=100, null=True, blank=True)
    display = models.CharField(max_length=100, null=True, blank=True)
    battery_life = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name
