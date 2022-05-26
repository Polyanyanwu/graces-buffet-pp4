""" Booking form for the booking / home page """
import sys
from django import forms
from django.shortcuts import get_object_or_404
from general_tables.models import SystemPreference
from .models import Booking
from .widget import DatePickerInput


def get_seat_options():
    """ Retrieve the maximum persons for online booking
        as provided in System preferences
    """
    total_people = get_object_or_404(SystemPreference, code='M')
    tot_person = total_people.data
    seat_options = []
    for i in range(1, tot_person + 1):
        seat_options.append((i, str(i) + ' people'))
    return seat_options


class BookingForm(forms.ModelForm):
    """ Booking form, define seats to enable
        dynamic population of the persons options
    """
    if 'test' in sys.argv:
        # when running test, calling the get_seat_options fail
        SEAT_OPTIONS = [
                (1, '1 People'),
                (2, '2 People'),
                (3, '3 People'),
                (4, '4 People'),
                (6, '6 People'),
                (7, '7 People'),
                (8, '8 People'),
                (9, '9 People'),
        ]
        seats = forms.ChoiceField(choices=SEAT_OPTIONS)
        dinner_date = forms.DateTimeField()
    else:
        seats = forms.ChoiceField(choices=get_seat_options())

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['seats'].choices = get_seat_options()

    class Meta:
        """ Specify the model to use and HTML5 date picker """
        model = Booking
        exclude = ['cancelled_by']
        widgets = {
            'dinner_date': DatePickerInput(),
        }


class UpdateBookingForm(forms.ModelForm):
    """ Booking form to update after service
    """
    class Meta:
        """ Specify the model to use and HTML5 date picker """
        model = Booking
        fields = ['booking_status']
