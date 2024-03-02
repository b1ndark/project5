from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class Reviews(models.Model):
    """
    Product reviews
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'
