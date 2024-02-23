from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'default_country', 'fav_brand', 'fav_os',
    )

    ordering = (
        'user', 'default_country', 'fav_brand', 'fav_os',)


admin.site.register(UserProfile, UserProfileAdmin)
