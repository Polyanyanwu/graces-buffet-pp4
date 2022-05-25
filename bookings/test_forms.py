""" Form testing class """
from django.test import TestCase
from general_tables.models import SystemPreference
from .forms import BookingForm


class TesItemForm(TestCase):
    """ Form testing class"""

    def setUp(self):
        SystemPreference.objects.create(code="M", data='8')

    def test_dinner_date_is_required(self):
        """ test dinner date on the form is required """
        form = BookingForm({'dinner_date': '', 'seats': 3})
        self.assertFalse(form.is_valid())
        self.assertIn('dinner_date', form.errors.keys())
