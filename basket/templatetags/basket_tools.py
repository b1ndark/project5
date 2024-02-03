from django import template

"""
calc subtotal template filter
"""
register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
