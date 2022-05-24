"""
Signals that listen for bookings
"""
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Booking


@receiver(post_save, sender=Booking)
def send_email_confirmation_of_booking(sender, instance, created, **kwargs):
    """ Send email confirmation when user booked successfully"""
    if created:
        instance.confirm_booking_send_email()


@receiver(post_save, sender=Booking)
def send_email_for_cancelled_booking(sender, instance, created, **kwargs):
    """ Send email confirmation when booking is cancelled successfully"""
    if not created and instance.booking_status.code == 'C':
        instance.cancel_booking_send_email()


@receiver(post_save, sender=Booking)
def send_email_for_edited_booking(sender, instance, created, **kwargs):
    """ Send email confirmation when booking is edited successfully"""
    if not created and instance.booking_status.code != 'C' and (
            instance.booking_status.code == 'B' and instance.edited):
        instance.modify_booking_send_email()
