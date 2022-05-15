""" Database tables for the booking functionality """

from django.db import models
import django.utils.timezone
from django.contrib.auth.models import User
from general_tables.models import \
    BuffetPeriod, BookingStatus, DiningTable, SystemPreference


def get_total_people():
    """ Retrieve the maximum persons for online booking
        requires app restart when changed by the Admin"""
    total_peoples = SystemPreference.objects.filter(code__exact='M').values()
    return total_peoples[0]['data'] if total_peoples[0]['data'] > 0 else 10


class Booking(models.Model):
    """ Main bookings table"""

    SEAT_OPTIONS = []
    tot_person = get_total_people()
    for i in range(1, tot_person + 1):
        SEAT_OPTIONS.append((i, str(i) + ' people'))

    booked_for = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name="booked_for", blank=True,
                                   null=True)
    dinner_date = models.DateTimeField(default=django.utils.timezone.now,
                                       blank=False)
    start_time = models.ForeignKey(BuffetPeriod,
                                   on_delete=models.CASCADE, default=1)
    seats = models.PositiveSmallIntegerField(blank=False,
                                             default=1, choices=SEAT_OPTIONS)
    booked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                  blank=True, related_name="booked_by")
    booking_status = models.ForeignKey(BookingStatus, on_delete=models.CASCADE,
                                       blank=True, null=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    date_cancelled = models.DateTimeField(blank=True, null=True)
    cancelled_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name="cancelled_by")
    fulfilled_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name="fulfilled_by")
    date_fulfilled = models.DateTimeField(blank=True, null=True)

    class Meta:
        " display times in ascending order"
        ordering = ["-booking_date", 'start_time']

    def __str__(self):
        return f"{self.booked_for} {self.booking_date} {self.start_time}"


class TablesBooked(models.Model):
    """ tables used in making the booking """
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    # don't delete a table if it has bookings
    table_id = models.ForeignKey(DiningTable, on_delete=models.PROTECT)
    seats_booked = models.PositiveSmallIntegerField(default=0)
    date_booked = models.DateField(auto_now=True)
    time_booked = models.TimeField(null=True)

    def __str__(self):
        return f"{self.table_id}"
