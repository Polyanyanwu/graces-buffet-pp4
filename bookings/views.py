from datetime import timedelta, datetime, date
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db import transaction, IntegrityError

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Sum
from cuisine.models import Cuisine, CuisineChoice
from general_tables.models import DiningTable, BuffetPeriod, SystemPreference, BookingStatus
from .models import Booking, TablesBooked
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
                                             request.POST.get('dinner_date'),
                                             time_entered)
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
                                time_booked=time_entered.start_time,
                                table_capacity=table_item.total_seats)

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
        price_queryset = SystemPreference.objects.get(code="P")
        buffet_price = price_queryset.data
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

    def book_seats(self, seats, day_booked, start_time):
        """ Check availability of seats and book if found
            return a dictionary of the tables/seats booked
        """
        booked = {}
        # fetch total seats in restaurant
        total_seats_dict = DiningTable.objects.all().aggregate(
                            Sum('total_seats'))
        total_seats = total_seats_dict['total_seats__sum']

        # Get duration of each buffet service D

        duration_qs = SystemPreference.objects.get(code="D")
        duration = duration_qs.data

        start_period_dt = datetime.combine(date.today(
            ), start_time.start_time) - timedelta(minutes=duration)
        start_period = start_period_dt.time()
        end_period_dt = datetime.combine(date.today(), start_time.start_time)\
            + timedelta(minutes=duration)
        end_period = end_period_dt.time()

        day_booked_dt = datetime.strptime(day_booked, "%Y-%m-%d").date()

        total_booked_on_day = TablesBooked.objects.filter(
            time_booked__gte=start_period,
            time_booked__lte=end_period,
            date_booked=day_booked_dt).aggregate(
            sum_booked=Sum('seats_booked'))

        seats_already_booked = total_booked_on_day['sum_booked']\
            if total_booked_on_day['sum_booked'] else 0
        available = total_seats - seats_already_booked

        # check which tables have vacant seats by getting their
        # installed capacity from DiningTables - used seats from TablesBooked
        booked_tabs_qs = TablesBooked.objects.filter(
            date_booked=day_booked_dt,
            time_booked__gte=start_period,
            time_booked__lte=end_period)\
            .values('table_id', 'table_capacity').order_by('table_id')\
            .annotate(total_seat=Sum('seats_booked'))

        # dictionary of table_id, table capacity and total seats used
        booked_tables = {}
        for item in booked_tabs_qs:
            booked_tables[item['table_id']] = [item['table_capacity'],
                                               item['total_seat']]

        tables = DiningTable.objects.all()
        tables_available = {}
        for table in tables:
            t_id = table.id
            if booked_tables.get(t_id):
                if booked_tables[t_id][0] - booked_tables[t_id][1] > 0:
                    tables_available[table] =\
                        booked_tables[t_id][0] - booked_tables[t_id][1]
            else:
                tables_available[table] = table.total_seats
        sort_tables_available = dict(sorted(tables_available.items(),
                                            key=lambda x: x[1], reverse=True))
        if seats > available:
            return booked
        print(total_seats, total_booked_on_day, available)

        for table_a, seats_a in sort_tables_available.items():
            # check to see if you get an exact table matching the seats needed
            if seats_a == seats:
                booked.clear()
                booked[table_a] = seats_a
                return booked
            # check to see if you get a table having enough seats to match need
            # keep replacing the higher capacity seats till the least one
            elif seats_a > seats:
                booked.clear()
                booked[table_a] = seats_a

        # if after checking we can't get a table with enough seats
        # comnine tables with largest space until need is met
        allocated = 0
        if len(booked) == 0:
            for table_a, seats_a in sort_tables_available.items():
                remaining = seats_a
                if remaining > 0:
                    if seats - allocated <= remaining:
                        remaining = seats - allocated
                    booked[table_a] = remaining
                    allocated += remaining
                    if allocated == seats:
                        break
        return booked
