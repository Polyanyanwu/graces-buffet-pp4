""" Contact form for receiving messages """
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Configure the contact form """
    subject = forms.CharField(label='Subject',
                              widget=forms.TextInput(
                               attrs={'placeholder': 'Subject'}))
    message_body = forms.CharField(label='Your message',
                                   widget=forms.TextInput(
                                    attrs={'placeholder':
                                           'Your detailed message please'}))
    sender = forms.EmailField(label='Email Address',
                              widget=forms.TextInput(
                               attrs={'placeholder': 'Email address'}))

    class Meta:
        """ Form meta class """
        model = Contact
        fields = ('subject', 'sender', 'message_body', )
