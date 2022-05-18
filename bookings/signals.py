"""
Signals that listen for bookings
"""
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Booking


@receiver(post_save, sender=Booking)
def send_email_confirmation_of_booking(sender, instance, created, **kwargs):
    """ Send email confirmation when user booked successfully"""
    print("created===", created)
    if created:
        instance.confirm_booking_send_email()
