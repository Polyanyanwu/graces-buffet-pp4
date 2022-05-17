""" Database tables for the booking functionality """

from django.db import models
import django.utils.timezone
from django.contrib.auth.models import User
from general_tables.models import \
    BuffetPeriod, BookingStatus, DiningTable


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
    table_capacity = models.PositiveSmallIntegerField()
    seats_booked = models.PositiveSmallIntegerField(default=0)
    date_booked = models.DateField(auto_now=True)
    time_booked = models.TimeField(null=True)

    def __str__(self):
        return f"{self.table_id}"
