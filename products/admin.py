from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'sku',
        'brand',
        'operating_system',
        'memory_ram',
        'display',
        'battery_life',
        'category',
        'rating',
        'price',
        'created',
        'updated',
    )

    ordering = ('brand', 'operating_system', 'sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
