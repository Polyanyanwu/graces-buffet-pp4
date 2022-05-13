from django.shortcuts import render
from django.views import View
from cuisine.models import Cuisine
from .models import Booking, SystemPreference


class MakeBookings(View):

    def get(self, request, *args, **kwargs):
        price_queryset = SystemPreference.objects.filter(code="P").values()
        buffet_price = price_queryset[0]['data']
        booking = Booking.objects.all()
        cuisine_queryset = Cuisine.objects.all()

        return render(
            request,
            "bookings/make_booking.html",
            {
                "buffet_price": buffet_price,
                "booking": booking,
                "cuisines": cuisine_queryset
            }
        )
