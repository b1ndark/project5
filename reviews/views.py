from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Reviews


@login_required
def add_review(request):
    """
    Add a product to the store inventory
    Also check if User is Superuser
    """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(
                request, 'The new Item has been added to the store inventory')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add the product, please check the form!')
    else:
        form = ProductForm()

    template = 'products/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
