""" model for general tables used in the application """

from django.db import models


class BookingStatus(models.Model):
    """ booking status list maintained by admin/operator"""
    BOOKING_OPTIONS = [
            ('B', 'Booked'),
            ('F', 'Fulfilled'),
            ('C', 'Cancelled'),
        ]

    code = models.CharField(primary_key=True, choices=BOOKING_OPTIONS,
                            default='B', max_length=1)
    description = models.CharField(max_length=20, unique=True, blank=False)

    def __str__(self):
        return str(self.description)


class BuffetPeriod(models.Model):
    """ start time slots for buffet bookings maintained by admin/operator"""
    start_time = models.TimeField(unique=True, blank=False)

    class Meta:
        " display times in ascending order"
        ordering = ["start_time"]

    def __str__(self):
        return str(self.start_time)


class SystemPreference(models.Model):
    """ Variables for system to operate
        Maintained by the Administrator"""
    SYSTEM_OPTIONS = [
            ('D', 'Duration of each Buffet Service'),
            ('N', 'No Show Time Duration Minutes'),
            ('C', 'Cancellation Notice Minutes'),
            ('P', 'Buffet Price per Person'),
            ('M', 'Max Persons per Online Booking'),
        ]

    code = models.CharField(primary_key=True, choices=SYSTEM_OPTIONS,
                            default='P', max_length=1)
    data = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return str(self.code)

    # def get_preference_name(self):
    #     """ return the data """
    #     return self.data

    # def pref_verbose(self):
    #     return dict(SystemPreference.SYSTEM_OPTIONS)[self.code]


class DiningTable(models.Model):
    """ Dining tables maintenance """
    location = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=50, blank=False)
    total_seats = models.PositiveIntegerField(blank=False,)
    used_seats = models.PositiveIntegerField(blank=False, default=0)

    class Meta:
        " display times in ascending order"
        ordering = ["total_seats"]

    def seats_remaining(self):
        """ Compute and return total seats remaining """
        return self.total_seats - self.used_seats

    def __str__(self):
        return str(self.description)


class HomeMessage(models.Model):
    """ Description of messages for Terms of Use and Privacy Policy """
    CHOICES = [
        ('T', 'Terms of Use'),
        ('P', 'Privacy Policy')
    ]

    code = models.CharField(max_length=1, primary_key=True, choices=CHOICES)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.description)
