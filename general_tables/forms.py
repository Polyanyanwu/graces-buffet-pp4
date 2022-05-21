from django import forms
from .models import SystemPreference


class SystemPreferenceForm(forms.ModelForm):
    """ Update system preferences data """
    class Meta:
        """ Specify the model to update """
        model = SystemPreference
        fields = ('code', 'data')
        readonly_fields = ('code',)
