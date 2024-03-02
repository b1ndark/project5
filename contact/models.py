from django.db import models


class Contact(models.Model):
    """
    Contact Model
    """

    class Meta:
        verbose_name_plural = 'User Contacts'

    name = models.CharField(max_length=100)
    emailaddress = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
