from django.contrib import admin
from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created',
        'updated',
    )


admin.site.register(About, AboutAdmin)
