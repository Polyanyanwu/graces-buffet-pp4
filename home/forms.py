""" Contact form for receiving messages """
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Configure the contact form """

    sender = forms.EmailField(label='Email Address',
                              widget=forms.TextInput(
                               attrs={'placeholder': 'Email address'}))

    class Meta:
        """ Form meta class """
        model = Contact
        fields = ('subject', 'sender', 'message_body', )
