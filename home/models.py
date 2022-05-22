""" Models for Contact message """

from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


class Contact(models.Model):
    """ Data model for contact us """

    options = [
            ('Information', 'Information'),
            ('Cuisine', 'Cuisine'),
            ('Seating', 'Seating'),
            ('Others', 'Others'),
        ]

    subject = models.CharField(choices=options, default='Information',
                               max_length=200, null=False, blank=False)
    message_body = models.TextField(null=False, blank=False)
    sender = models.EmailField(max_length=200, null=False, blank=False)
    date_time = models.DateTimeField(auto_now_add=True)
    # user could be guest
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True)

    def __str__(self):
        return str(self.sender)

    def send_email_message(self):
        """
        Send confirmation email when a contact completes a contact form """

        sender = self.sender
        subject = 'Message well received'
        body = render_to_string(
            'home/confirmation/contact_confirmation.txt',
            {'details': self})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [sender]
        )
