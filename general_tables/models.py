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
    status = models.CharField(max_length=20, unique=True, blank=False)

    def __str__(self):
        return self.status
