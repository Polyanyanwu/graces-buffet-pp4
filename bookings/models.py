""" Database tables for the booking functionality """

from datetime import datetime
from django.db import models
import django.utils.timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from general_tables.models import \
    BuffetPeriod, BookingStatus, DiningTable, SystemPreference


class Booking(models.Model):
    """ Main bookings table"""

    booked_for = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name="booked_for", blank=True,
                                   null=True)
    dinner_date = models.DateTimeField(default=django.utils.timezone.now,
                                       blank=False)
    start_time = models.ForeignKey(BuffetPeriod,
                                   on_delete=models.CASCADE, default=1)
    seats = models.PositiveSmallIntegerField(blank=False, default=1)
    booked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                  blank=True, related_name="booked_by")
    booking_status = models.ForeignKey(BookingStatus, on_delete=models.CASCADE,
                                       blank=True, null=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    cuisines = models.CharField(max_length=150, unique=False, blank=True)
    date_cancelled = models.DateTimeField(blank=True, null=True)
    cancelled_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name="cancelled_by")
    fulfilled_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name="fulfilled_by")
    date_fulfilled = models.DateTimeField(blank=True, null=True)
    edited = models.BooleanField(default=False)

    class Meta:
        " display times in ascending order"
        ordering = ["-booking_date", 'start_time']

    def __str__(self):
        return f"{self.booked_for} {self.booking_date} {self.start_time}"

    def confirm_booking_send_email(self):
        """ Send email confirmation when a booking is created """

        user_profile = User.objects.get(username=self.booked_for)
        customer_email = user_profile.email

        #  Get no show time from general tables settings
        duration = get_no_show_time()
        dinner_date = django.utils.timezone.localtime(self.dinner_date)
        subject = 'Booking Confirmation'
        body = render_to_string(
                'bookings/confirmation/confirmation_email.txt',
                {'dinner_date': dinner_date.strftime("%d %b, %Y"),
                 'contact_email': settings.DEFAULT_FROM_EMAIL,
                 'start_time': self.start_time,
                 'seats': self.seats,
                 'username': user_profile.get_full_name(),
                 'show_up_time': duration})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    # Write notification record
        Notification.objects.create(
            subject=subject + ": " + user_profile.get_full_name(),
            message=body,
            user=user_profile)

    def cancel_booking_send_email(self):
        """ Send email confirmation when a booking is cancelled """

        user_profile = User.objects.get(username=self.booked_for)
        customer_email = user_profile.email
        dinner_date = django.utils.timezone.localtime(self.dinner_date)
        subject = 'Cancellation of Booking'
        body = render_to_string(
                'bookings/confirmation/cancellation_email.txt',
                {'dinner_date': dinner_date.strftime("%d %b, %Y"),
                 'contact_email': settings.DEFAULT_FROM_EMAIL,
                 'start_time': self.start_time,
                 'seats': self.seats,
                 'username': user_profile.get_full_name()})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )
    # Write notification record
        Notification.objects.create(
            subject=subject + ": " + user_profile.get_full_name(),
            message=body,
            user=user_profile)

    def modify_booking_send_email(self):
        """
            Send email  confirmation when a booking is edited by customer
        """
        user_profile = User.objects.get(username=self.booked_for)
        customer_email = user_profile.email
        duration = get_no_show_time()
        edited_date = datetime.now()
        dinner_date = datetime.strptime(self.dinner_date, "%Y-%m-%d").date()
        subject = 'Edited Booking Confirmation'
        body = render_to_string(
                'bookings/confirmation/edit_booking_email.txt',
                {'dinner_date': dinner_date.strftime("%d %b, %Y"),
                 'contact_email': settings.DEFAULT_FROM_EMAIL,
                 'start_time': self.start_time,
                 'seats': self.seats,
                 'username': user_profile.get_full_name(),
                 'edited_date': edited_date.strftime("%d %b, %Y %H:%M"),
                 'show_up_time': duration})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    # Write notification record
        Notification.objects.create(
            subject=subject + ": " + user_profile.get_full_name(),
            message=body,
            user=user_profile)


class TablesBooked(models.Model):
    """ tables used in making the booking """
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    # don't delete a table if it has bookings
    table_id = models.ForeignKey(DiningTable, on_delete=models.PROTECT)
    table_capacity = models.PositiveSmallIntegerField()
    seats_booked = models.PositiveSmallIntegerField(default=0)
    date_booked = models.DateField(null=False)
    time_booked = models.TimeField(null=True)

    def __str__(self):
        return f"{self.table_id}"


class Notification(models.Model):
    """ Notifications detail records """
    notice_date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=200, blank=False)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="notice_for")

    def __str__(self):
        return str(self.subject)


def get_no_show_time():
    """ Retrieve the No show time duration from System Preferences """
    try:
        duration_qs = SystemPreference.objects.get(code="N")
        return duration_qs.data
    except ObjectDoesNotExist:
        return 60
