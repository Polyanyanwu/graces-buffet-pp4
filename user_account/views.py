""" Profile and Group update view """

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import User, Group
from .forms import ProfileForm, UserForm, GroupForm
from .user_auth import check_access


@login_required
@transaction.atomic
def update_profile(request):
    """ Update user profile """
    rights = check_access(request.user, ("administrator", ))
    if rights != "OK":
        messages.error(request, (rights))
        return redirect('/')
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
    """ Add or remove user from a group
        Only administrator group members have access to this """
    rights = check_access(request.user, ("administrator", ))
    if rights != "OK":
        messages.error(request, (rights))
        return redirect('/')
    if request.method == 'POST':
        if 'user_change' in request.POST:
            user_sent = request.POST.get('user')
            user = get_object_or_404(User, id=user_sent)
            group_form = GroupForm(instance=user)

        elif 'remove_group' in request.POST:
            my_group = Group.objects.get(
                name=request.POST.get('user_group_selected'))
            user_sent = request.POST.get('user')
            user = get_object_or_404(User, id=user_sent)
            my_group.user_set.remove(user)
            group_form = GroupForm(instance=user)
            messages.success(request, ('Group removed successfully'))

        elif 'add_user_group' in request.POST:
            print(request.POST)
            group_name = request.POST.get('group_name')
            user_sent = request.POST.get('user')
            user = get_object_or_404(User, id=user_sent)
            group_form = GroupForm(instance=user)

            if not group_name:
                messages.error(request,
                               ('Please select a group before clicking Add'))
                group_form = GroupForm()
            else:
                my_group = Group.objects.get(id=group_name)
                if check_access(user, (my_group.name, )) == "OK":
                    messages.error(request,
                                   ('User already in this group'))
                else:
                    my_group.user_set.add(user)
                    messages.success(request,
                                     ('Group added successfully'))
    else:
        user = request.user
        group_form = GroupForm()

    return render(request, 'profiles/user_group.html',
                  {
                        'group_form': group_form,
                        'users': user
                  })
