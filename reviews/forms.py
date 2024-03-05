from django import forms
from .models import Reviews


class ReviewsForm(forms.ModelForm):
    """
    To render a review form
    """

    class Meta:
        model = Reviews
        fields = (
            'review',
        )

        widgets = {
            'review': forms.Textarea(
                attrs={'rows': 6,
                       'style': 'resize:none',
                       'placeholder': 'Write a review...',
                       'aria-label': 'review'}),
        }
