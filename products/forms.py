from django import forms
from .models import Product, category


class ProductForm(forms.ModelForm):
    """ Form to add a product to the store inventory """

    class Meta:
        model = Product
        fields = (
            'category',
            'sku',
            'name',
            'brand',
            'operating_system',
            'memory_ram',
            'display',
            'battery_life',
            'description',
            'rating',
            'price',
            'image',
        )

    def __init__(self, *args, **kwargs):
        super().__init_(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'
