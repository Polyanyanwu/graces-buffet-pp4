""" Utility module for Bookings App """

from datetime import timedelta, datetime, date
from django.db.models import Sum, Q
from django.shortcuts import get_object_or_404
from general_tables.models import\
    (DiningTable, SystemPreference, BuffetPeriod, BookingStatus)
from .models import TablesBooked, Booking


def book_seats(seats, day_booked, start_time):
    """ Check availability of seats and book if found
        return a dictionary of the tables/seats booked
        Parameters:
            seats: no of seats to check availability
            day_booked: dinner date
            start_time: Start time for dinner
        Returns:
            a dict of the tables available for the booking
            or empty dictionary if fully booked
    """
    booked = {}
    # fetch total seats in restaurant
    total_seats_dict = DiningTable.objects.all().aggregate(
                        Sum('total_seats'))
    total_seats = total_seats_dict['total_seats__sum']

    # Get duration of each buffet service D
    duration_qs = get_object_or_404(SystemPreference, code="D")
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
    # combine tables with largest space until need is met
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


def is_dinner_date_in_future(dinner_date_str, start_time):
    """
    check that dinner date is in future or today
    if today check that time is in future
    Parameters:
        dinner_date_str: String of dinner date from POST
        start_time: start_time selected from POST
    Returns:
        A dictionary of the outcome message and time entered
    """
    answer = {}
    dinner_date = datetime.strptime(dinner_date_str, "%Y-%m-%d").date()
    now = datetime.now()
    time_entered_qs = BuffetPeriod.objects.filter(id=start_time)
    time_entered = get_object_or_404(time_entered_qs)
    if dinner_date < now.date():
        msg = 'Dinner date cannot be earlier than today'
    elif dinner_date == now.date() and \
            time_entered.start_time <= datetime.now().time():
        msg = 'Dinner time cannot be earlier than now for today'
    else:
        msg = "OK"
    answer['msg'] = msg
    answer['time_entered'] = time_entered
    return answer


def query_booking(request, req_type, calling_module, booking_status=None):
    """ Query the Booking table based on criteria entered by user
        If request type is post write the criteria to session
        If type is get, retrieve criteria from session
    Parameters:
        request : the request to extract the criteria from
        req_ty: a String of the request type
        calling_module: the function that called
        booking_status: some modules have fixed booking status
    Returns:
        filtered booking table
    """
    if req_type == 'get':
        query_dict = request.session.get(calling_module)
        if query_dict:
            sdate = query_dict['start_date']
            edate = query_dict['end_date']
            bstatus = query_dict['booking_status']
            username = query_dict['username']
            start_date = datetime.strptime(
                sdate, "%Y-%m-%d").date() if sdate else None
            end_date = datetime.strptime(
                edate, "%Y-%m-%d").date() if edate else None
        else:
            if booking_status:
                return Booking.objects.filter(
                    booking_status=booking_status).order_by('-booking_date')
            else:
                return Booking.objects.all().order_by('-booking_date')
    else:

        bstatus = request.POST.get('booking_status') if request.POST.get(
            'booking_status') else None
        if bstatus:
            book_status = BookingStatus.objects.get(code=bstatus)

        sdate = request.POST.get('dinner_date_start') if request.POST.get(
            'dinner_date_start') else None
        start_date = datetime.strptime(
            sdate, "%Y-%m-%d").date() if sdate else None

        edate = request.POST.get('dinner_date_end') if request.POST.get(
            'dinner_date_end') else None
        end_date = datetime.strptime(
            edate, "%Y-%m-%d").date() if edate else None

        username = request.POST.get('user_name') if request.POST.get(
            'user_name') else None
        query_dict = {}
        query_dict['start_date'] = sdate
        query_dict['end_date'] = edate
        query_dict['booking_status'] = bstatus
        query_dict['username'] = username
        request.session[calling_module] = query_dict

    if start_date and end_date and bstatus and username:
        booking = Booking.objects.filter(
            Q(dinner_date__gte=start_date) &
            Q(booking_status=bstatus) &
            Q(dinner_date__lte=end_date) &
            (Q(booked_for__first_name__icontains=username)
                | Q(booked_for__last_name__icontains=username))).order_by(
                    '-dinner_date')
    elif start_date and end_date and username:
        booking = Booking.objects.filter(
            Q(dinner_date__gte=start_date) &
            Q(dinner_date__lte=end_date) &
            (Q(booked_for__first_name__icontains=username)
                | Q(booked_for__last_name__icontains=username))).order_by(
                    '-dinner_date')
    elif start_date and end_date and bstatus:
        booking = Booking.objects.filter(
            dinner_date__gte=start_date,
            booking_status=bstatus,
            dinner_date__lte=end_date).order_by('-dinner_date')
    elif start_date and end_date:
        booking = Booking.objects.filter(
            dinner_date__gte=start_date,
            dinner_date__lte=end_date).order_by('-dinner_date')
    elif start_date:
        booking = Booking.objects.filter(dinner_date=start_date).order_by(
            '-dinner_date')
    elif end_date:
        booking = Booking.objects.filter(dinner_date=end_date).order_by(
            '-dinner_date')
    elif username:
        booking = Booking.objects.filter(
            Q(booked_for__first_name__icontains=username) | Q(
                booked_for__last_name__icontains=username)).order_by(
                    '-dinner_date')
    elif bstatus:
        booking = Booking.objects.filter(booking_status=book_status).order_by(
            '-dinner_date')
    else:
        booking = Booking.objects.all().order_by('-dinner_date')

    if booking_status:
        booking = booking.filter(booking_status=booking_status).order_by(
            '-dinner_date')
    return booking
