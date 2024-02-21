from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'default_country', 'fav_brand', 'fav_operating_system',
    )

    ordering = (
        'user', 'default_country', 'fav_brand', 'fav_operating_system',)


admin.site.register(UserProfile, UserProfileAdmin)
