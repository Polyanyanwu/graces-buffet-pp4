""" Widget for the Datetime picker """

from django import forms


class DatePickerInput(forms.DateInput):
    """ Widget for date """
    input_type = 'date'


class TimePickerInput(forms.TimeInput):
    """ Widget for time """
    input_type = 'time'


class DateTimePickerInput(forms.DateTimeInput):
    """ Widget for datetime """
    input_type = 'datetime'
