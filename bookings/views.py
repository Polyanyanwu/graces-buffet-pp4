from django.shortcuts import render, get_object_or_404
from django.views import View
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from cuisine.models import Cuisine
from .models import Booking, SystemPreference, BookingStatus  # , DiningTable
from .forms import BookingForm


class MakeBookings(View):

    def get(self, request, *args, **kwargs):
        price_queryset = SystemPreference.objects.filter(code="P").values()
        buffet_price = price_queryset[0]['data']
        booking = Booking.objects.filter(id=None)
        cuisine_queryset = Cuisine.objects.all()
        form = BookingForm()
        return render(
            request,
            "bookings/make_booking.html",
            {
                "buffet_price": buffet_price,
                "booking": booking,
                "cuisines": cuisine_queryset,
                "form": form
            }
        )

    def post(self, request, *args, **kwargs):
        # check if user is logged in
        if not request.user.is_authenticated:
            messages.add_message(request,
                                 messages.ERROR,
                                 'Please login first before you can complete a\
                                  booking. Click the Signup button above\
                                  or login\
                                  if you already have an account ')
            return
        user_profile = User.objects.get(username=request.user)
        booking_status_qs = BookingStatus.objects.filter(code="B")
        booking_status = get_object_or_404(booking_status_qs)
        booking = BookingForm(data=request.POST)

        # booking_form = BookingForm(data=update_booking)
        if booking.is_valid():
            booking.save(commit=False)
            booking.instance.booked_for = request.user
            booking.instance.booked_by = request.user
            booking.instance.booking_status = booking_status
            booking.save()
            messages.add_message(request, messages.INFO,
                                 'Thank you: Your booking has been confirmed.')
        else:
            booking_form = BookingForm()
            messages.add_message(request, messages.ERROR, 'Error occurred')

        # check availability of the dates
        cuisine_queryset = Cuisine.objects.all()
        price_queryset = SystemPreference.objects.filter(code="P").values()
        buffet_price = price_queryset[0]['data']
        print(request.POST.getlist('cuisine_option'))
        booking_form = BookingForm(data=request.POST)
        no_bookings = Booking.objects.filter(id=None)
        return render(
            request,
            "bookings/make_booking.html",
            {
                "buffet_price": buffet_price,
                "booking": no_bookings,
                "cuisines": cuisine_queryset,
                "form": booking_form
            }
        )
