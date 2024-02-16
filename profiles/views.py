from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages


def profile(request):
    """
    To render the profile page
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)


def edit_profile(request):
    """
    To render the edit profile form page
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your profile has been updated')
            return redirect(reverse('profile'))
    
    form = UserProfileForm(instance=profile)

    template = 'profiles/edit_profile.html'
    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, template, context)
