from django.shortcuts import render, get_object_or_404
from django.views import View
# from django.contrib.auth.decorators import login_required
from django.db import transaction, IntegrityError
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Sum, F

from cuisine.models import Cuisine, CuisineChoice
from general_tables.models import DiningTable, BuffetPeriod
from .models import Booking, SystemPreference, BookingStatus, TablesBooked
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
            return HttpResponseRedirect("/")
        user_profile = User.objects.get(username=request.user)
        booking_status_qs = BookingStatus.objects.filter(code="B")
        booking_status = get_object_or_404(booking_status_qs)
        booking = BookingForm(data=request.POST)

        if booking.is_valid():
            try:
                with transaction.atomic():
                    booking.save(commit=False)

                    time_entered_qs = BuffetPeriod.objects.filter(id=request.POST.get('start_time'))
                    time_entered = get_object_or_404(time_entered_qs)
                    # check seats availability
                    tables = self.book_seats(int(request.POST.get('seats')),
                                             request.POST.get('dinner_date'))
                    print("tables returned==", tables, type(tables))
                    if len(tables) == 0:
                        # no seats found on selected date
                        messages.add_message(request, messages.WARNING,
                                             'So sorry, Graces Buffet is fully booked\
                        on your chosen date and time. Try another date/time.')
                        return HttpResponseRedirect("/")
                    else:
                        # save booking first
                        booking.instance.booked_for = request.user
                        booking.instance.booked_by = request.user
                        booking.instance.booking_status = booking_status
                        booking.save()
                        # save tables booked
                        for table_item, seat in tables.items():
                            print("table item==", table_item, "seat==", seat)
                            TablesBooked.objects.create(
                                booking_id=booking.instance,
                                seats_booked=seat,
                                table_id=table_item,
                                time_booked=time_entered.start_time)

                            # Update the Dining Tables
                            table_item.used_seats += seat
                            table_item.save()
                            
                    # save the cuisine choices
                    cuisine_choices = request.POST.getlist('cuisine_option')
                    if len(cuisine_choices) > 0:
                        for choice in cuisine_choices:
                            cuisine_qs = Cuisine.objects.filter(id=choice)
                            cuisine_rec = get_object_or_404(cuisine_qs)
                            CuisineChoice.objects.create(
                                booking_id=booking.instance,
                                cuisine_id=cuisine_rec)
                    messages.add_message(request, messages.INFO,
                                         'Thank you: Your booking has\
                                          been confirmed.')
            except IntegrityError:
                messages.add_message(request, messages.WARNING,
                                     'Your booking could not be completed now\
                                     check your entry and try again.')
                return HttpResponseRedirect("/")
        else:
            booking_form = BookingForm()
            messages.add_message(request, messages.WARNING,
                                 'Your booking could not be completed now\
                                  check your entry and try again.')
            return HttpResponseRedirect("/")

        # check availability of the dates
        cuisine_queryset = Cuisine.objects.all()
        price_queryset = SystemPreference.objects.filter(code="P").values()
        buffet_price = price_queryset[0]['data']
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

    def book_seats(self, seats, day_booked):
        """ Check availability of seats and book if found
            return a dictionary of the tables/seats booked
        """
        booked = {}
        # fetch total seats in restaurant
        total_seats_dict = DiningTable.objects.all().aggregate(
                            Sum('total_seats'))
        total_seats = total_seats_dict['total_seats__sum']
        total_booked_on_day = TablesBooked.objects.filter(
                               date_booked=day_booked).aggregate(
                               Sum('seats_booked'))
        seats_already_booked = total_booked_on_day['seats_booked__sum']\
            if total_booked_on_day['seats_booked__sum'] else 0
        available = total_seats - seats_already_booked
        if seats > available:
            return booked
        print(total_seats, total_booked_on_day, available)
        # find the tables to use for the booking

        # din_tables_below = DiningTable.objects.annotate(
        #     diff=F('total_seats')
        #     - F('used_seats')).filter(diff__lte=seats).order_by('diff')

        dining_tables = DiningTable.objects.annotate(
            diff=F('total_seats')
            - F('used_seats')).order_by('-diff')
        print("Dining Tables", dining_tables)
        for table_item in dining_tables:
            # check to see if you get an exact table matching the seats needed
            if table_item.seats_remaining() == seats:
                booked.clear()
                booked[table_item] = table_item.seats_remaining()
                return booked
            # check to see if you get a table having enough seats to match need
            # used the minimum seats possible
            elif table_item.seats_remaining() > seats:
                booked.clear()
                booked[table_item] = table_item.seats_remaining()

        # if after checking we can't get a table with enough seats
        # comnine tables with largest space until need is met
        allocated = 0
        if len(booked) == 0:
            for table_item in dining_tables:
                remaining = table_item.seats_remaining()
                if seats - allocated <= remaining:
                    remaining = seats - allocated
                booked[table_item] = remaining
                allocated += remaining
                if allocated == seats:
                    break
        print(booked)
        return booked
