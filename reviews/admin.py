from django.contrib import admin
from .models import Reviews


class ReviewsAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'product',
        'created',
    )

admin.site.register(Reviews, ReviewsAdmin)
