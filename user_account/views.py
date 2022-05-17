""" Profile update view """

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .forms import ProfileForm, UserForm, GroupForm
# from .models import Profile


@login_required
@transaction.atomic
def update_profile(request):
    # profile_form = get_or_create(ProfileForm, user=request.user)
    # profile_form, created = Profile.objects.get_or_create(user_id=request.user)
    # print("created====", created)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,
                             ('Your profile was successfully updated!'))
            return redirect('/')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
@transaction.atomic
def update_group(request):
    # profile_form = get_or_create(ProfileForm, user=request.user)
    # profile_form, created = Profile.objects.get_or_create(user_id=request.user)
    # print("created====", created)
    if request.method == 'POST':
        # user_form = UserForm(request.POST, instance=request.user)
        # profile_form = ProfileForm(request.POST, instance=request.user.profile)
        # if user_form.is_valid() and profile_form.is_valid():
        #     user_form.save()
        #     profile_form.save()
        #     messages.success(request,
        #                      ('Your profile was successfully updated!'))
        #     return redirect('/')
        # else:
        messages.error(request, ('Testing correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        group_form = GroupForm(instance=request.user.profile)
    return render(request, 'profiles/user_group.html', {
        'user_form': user_form,
        'group_form': group_form
    })
