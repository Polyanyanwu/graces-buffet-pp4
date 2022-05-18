""" Booking form for the home page """
from django import forms
from django.shortcuts import get_object_or_404
from general_tables.models import SystemPreference
from .models import Booking
from .widget import DatePickerInput


def get_seat_options():
    """ Retrieve the maximum persons for online booking
        as provided in System preferences, default to
        8 if not set"""
    tot_person = 8
    total_people_qs = SystemPreference.objects.filter(code='M')
    total_people = get_object_or_404(total_people_qs)
    tot_person = total_people.data
    seat_options = []
    for i in range(1, tot_person + 1):
        seat_options.append((i, str(i) + ' people'))
    return seat_options


class BookingForm(forms.ModelForm):
    """ Booking form, define seats to enable
        dynamic population of the persons options
    """
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

# class DisplayBookingConfirmForm(forms.ModelForm):
#     """ display confirmation to user after booking success """
