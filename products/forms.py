from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


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
            'weight',
            'description',
            'rating',
            'price',
            'image',
        )

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'
