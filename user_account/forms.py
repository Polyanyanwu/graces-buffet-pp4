""" Custom form for user creation """

from django.contrib.auth.models import User, Group
from django import forms
from allauth.account.forms import SignupForm
from .models import Profile, UserGroup


class CustomSignupForm(SignupForm):
    """ Custom signup form """
    first_name = forms.CharField(max_length=30, label='First Name',
                                 required=True, widget=forms.TextInput(
                                  attrs={'placeholder': 'First name'}))

    last_name = forms.CharField(max_length=30, label='Last Name',
                                required=True, widget=forms.TextInput(
                                 attrs={'placeholder': 'Last name'}))

    field_order = ['username', 'first_name', 'last_name', 'email', 'password']

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class UserForm(forms.ModelForm):
    """ Update User form data """
    class Meta:
        """ Fields to update from User model """
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    """ Update profile data """
    class Meta:
        """ Specify the profile fields to update """
        model = Profile
        fields = ('phone', 'special_request')


class GroupForm(forms.ModelForm):
    """ Update profile data """
    class Meta:
        """ Specify the profile fields to update """
        model = UserGroup
        fields = ('user', 'group_name')

