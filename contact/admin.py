from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'emailaddress',
        'subject',
        'created_at',
    )


admin.site.register(Contact, ContactAdmin)
