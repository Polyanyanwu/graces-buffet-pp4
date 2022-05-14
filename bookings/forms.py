from django import forms
from .models import Booking
from .widget import DatePickerInput


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        exclude = ['cancelled_by']

        widgets = {
            'dinner_date': DatePickerInput(),
            # 'my_date_time_field' : DateTimePickerInput(),
        }
