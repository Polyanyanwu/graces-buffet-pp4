from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import SystemPreference, HomeMessage


class SystemPreferenceForm(forms.ModelForm):
    """ Update system preferences data """
    class Meta:
        """ Specify the model to update """
        model = SystemPreference
        fields = ('code', 'data')
        readonly_fields = ('code',)


class HomeMessageForm(forms.Form):
    model = HomeMessage
    description = forms.CharField(widget=SummernoteWidget())
