""" Database tables for maintaining cuisines and
    cuisines selected by customers """

from django.db import models
from cloudinary.models import CloudinaryField
from bookings.models import Booking


class Cuisine(models.Model):
    """ cuisine types available in the restaurant """
    name = models.CharField(max_length=50, unique=True, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    cuisine_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """ Sort by the name ascending """
        ordering = ["name"]

    def __str__(self):
        return str(self.name)


class CuisineChoice(models.Model):
    """ cuisine choices made by user """
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    cuisine_id = models.ForeignKey(Cuisine, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cuisine_id)
