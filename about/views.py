from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import About
from .forms import EditAboutForm


def about(request):
    """
    This will render the About page
    """

    return render(request, 'about/about.html')


@login_required
def edit_about(request):
    """
    Render a form to edit about page/footer
    Also checks if User is SuperUser/Admin
    """

    if not request.user.is_superuser:
        messages.error(
            request, 'You are not authorised to access Admin areas!')
        return redirect(reverse('home'))

    about = get_object_or_404(About)

    if request.method == 'POST':
        form = EditAboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            messages.success(request, 'About has been updated')
            return redirect(reverse('about'))
        else:
            messages.error(
                request, 'Update failed.\
                 Please make sure that the form is valid.')
    else:
        form = EditAboutForm(instance=about)

    template = 'about/edit_about.html'
    context = {
        'form': form,
        'about': about,
    }

    return render(request, template, context)
