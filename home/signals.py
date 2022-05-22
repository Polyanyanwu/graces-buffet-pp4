"""
Signals that listen for contact message
"""
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Contact


@receiver(post_save, sender=Contact)
def send_email_confirmation_of_contact(sender, instance, created, **kwargs):
    """ Send email confirmation when user contacts successfully"""
    if created:
        instance.send_email_contact_message()
