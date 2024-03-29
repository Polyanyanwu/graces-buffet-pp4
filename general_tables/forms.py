""" Forms for the System Preferences and Home message
    THe home message table is used to store the Terms of Use
    and Privacy Notice
"""
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import SystemPreference, HomeMessage


class SystemPreferenceForm(forms.ModelForm):
    """ Update system preferences data """
    class Meta:
        """ Specify the model to update """
        model = SystemPreference
        fields = ('code', 'data')
        readonly_fields = ('code',)


class HomeMessageForm(forms.Form):
    """ Privacy Notice and Terms of Use data """
    model = HomeMessage
    description = forms.CharField(widget=SummernoteWidget())
    fields = ('code', 'description')
