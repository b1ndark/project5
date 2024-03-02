from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Reviews
from .forms import ReviewsForm


@login_required
def edit_review(request, review_id):
    """
    To render Edit review form
    """

    review = get_object_or_404(Reviews, pk=review_id)
    if request.user != review.user:
        messages.error(
            request, 'This is not your review!')
        return redirect(reverse('home'))

    product = review.product
    form = ReviewsForm(instance=review)

    if request.method == 'POST':
        form = ReviewsForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            messages.success(
                request, 'The review has been updated')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to edit the review, please check the form!')
    else:
        form = ReviewsForm(instance=review)

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """
    To render Delete review template
    """
    review = get_object_or_404(Reviews, pk=review_id)
    if request.user != review.user:
        messages.error(
            request, 'This is not your review!')
        return redirect(reverse('home'))
    product = review.product

    if request.method == 'POST':
        review.delete()
        messages.success(
            request, 'The review has been deleted')
        return redirect(reverse('product_detail', args=[product.id]))

    template = 'reviews/delete_review.html'
    context = {
        'review': review,
        'product': product,
    }

    return render(request, template, context)
