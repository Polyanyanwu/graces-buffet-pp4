""" Module for the make, delete, edit, update, and queries on bookings """

from datetime import timedelta, datetime
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import View
from django.core.exceptions import EmptyResultSet
from django.db import transaction, IntegrityError
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from cuisine.models import Cuisine, CuisineChoice
from general_tables.models import BuffetPeriod, SystemPreference, BookingStatus
from user_account.user_auth import check_access
from .models import Booking, TablesBooked
from .forms import BookingForm, UpdateBookingForm
from .utils import book_seats, is_dinner_date_in_future, query_booking


class MakeBookings(View):
    """ Booking main page """

    def get(self, request, *args, **kwargs):
        """ Display the price per person and the booking form """

        price_queryset = get_object_or_404(SystemPreference, code="P")
        buffet_price = price_queryset.data
        booking = Booking.objects.filter(id=None)  # empty form
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

        booking_status_qs = BookingStatus.objects.filter(code="B")
        booking_status = get_object_or_404(booking_status_qs)
        booking = BookingForm(data=request.POST)

        cuisine_choices = request.POST.getlist('cuisine_option')
        if len(cuisine_choices) == 0:
            messages.add_message(request, messages.WARNING,
                                 'Please select one or more cuisine\
                                      choices before proceeding')
            return HttpResponseRedirect("/")

        if booking.is_valid():
            # check that dinner date is in future or today
            # if today check that time is in future
            dinner_date_str = request.POST.get('dinner_date')
            stime = request.POST.get('start_time')
            ans = is_dinner_date_in_future(dinner_date_str, stime)
            if ans['msg'] != "OK":
                messages.add_message(request, messages.WARNING, ans['msg'])
                return redirect('home')
            time_entered = ans['time_entered']
            try:
                # check if operator is booking for someone
                username = request.POST.get('username')
                if username:
                    user_to_book = User.objects.get(username=username)
                else:
                    user_to_book = request.user
                with transaction.atomic():
                    booking.save(commit=False)

                    # check seats availability
                    tables = book_seats(int(request.POST.get('seats')),
                                        request.POST.get('dinner_date'),
                                        time_entered)
                    if len(tables) == 0:
                        # no seats found on selected date
                        messages.add_message(request, messages.WARNING,
                                             'So sorry, Graces Buffet is fully booked\
                        on your chosen date and time. Try another date/time.')
                        return HttpResponseRedirect("/")
                    else:
                        # save booking first
                        booking.instance.booked_for = user_to_book
                        booking.instance.booked_by = request.user
                        booking.instance.booking_status = booking_status
                        booking.save()
                        # save tables booked
                        for table_item, seat in tables.items():
                            TablesBooked.objects.create(
                                booking_id=booking.instance,
                                seats_booked=seat,
                                table_id=table_item,
                                time_booked=time_entered.start_time,
                                date_booked=booking.instance.dinner_date,
                                table_capacity=table_item.total_seats)

                    # save the cuisine choices
                    cuisines = ""
                    if len(cuisine_choices) > 0:
                        for choice in cuisine_choices:
                            cuisine_qs = Cuisine.objects.filter(id=choice)
                            cuisine_rec = get_object_or_404(cuisine_qs)
                            cuisines += cuisine_rec.name + ", "
                            CuisineChoice.objects.create(
                                booking_id=booking.instance,
                                cuisine_id=cuisine_rec)
                            booking.instance.cuisines = cuisines[:-2]
                            booking.save()
                    messages.add_message(request, messages.INFO,
                                         'Thank you: Your booking has\
                                          been confirmed.')
                    return HttpResponseRedirect(reverse('booking_confirm',
                                                args=[booking.instance.id]))
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

        cuisine_queryset = Cuisine.objects.all()
        price_queryset = get_object_or_404(SystemPreference, code="P")
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


class MakeBookingsOthers(View):
    """ Booking main page for booking for others
        It has only a get method and reuses the post
        method for the MakeBooking
    """

    def get(self, request, username, *args, **kwargs):
        """ Display the price per person and the booking form """
        # check that user is operator or administrator
        rights = check_access(request.user, ("operator", "administrator"))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')

        price_queryset = get_object_or_404(SystemPreference, code="P")
        buffet_price = price_queryset.data
        booking = Booking.objects.filter(id=None)  # empty form
        cuisine_queryset = Cuisine.objects.all()
        form = BookingForm()

        user_to_book = User.objects.get(username=username)
        user_fullname = user_to_book.get_full_name()

        return render(
            request,
            "bookings/others/make_booking_others.html",
            {
                "buffet_price": buffet_price,
                "booking": booking,
                "cuisines": cuisine_queryset,
                "form": form,
                "username":  username,
                "user_fullname": user_fullname
            }
        )


class DisplayBookingConfirm(View):
    """ Display confirmation of booking to user """
    def get(self, request, booking_id, *args, **kwargs):
        """ Get method to display confirmation
            message after a successful booking
            Parameter:
                booking_id is passed by the calling template
        """
        if not request.user.is_authenticated:
            messages.add_message(request,
                                 messages.ERROR,
                                 'Please login first before you can access this page\
                                  Click the Signup button above\
                                  or login if you already have an account ')
            return HttpResponseRedirect("/")

        booking_qs = Booking.objects.select_related(
            'booked_for').filter(id=booking_id)
        booking = get_object_or_404(booking_qs)
        username_qs = User.objects.get(username=booking.booked_for)
        username = username_qs.get_full_name()
        cuisines_qs = CuisineChoice.objects.filter(booking_id=booking_id)
        cuisines = []
        for cus in cuisines_qs:
            cuisine_rec = Cuisine.objects.get(name=cus.cuisine_id)
            ci_map = {}
            ci_map["cuisine_image"] = cuisine_rec.cuisine_image
            ci_map["name"] = cuisine_rec.name
            cuisines.append(ci_map)

        return render(
            request,
            "bookings/display_booking_confirm.html",
            {
                "booking": booking,
                "username": username,
                "cuisines": cuisines
            }
        )


class BookingDetail(View):
    """ view booking details history """

    def get(self, request, *args, **kwargs):
        """ View booking dining history """

        # check that user is logged in
        rights = check_access(request.user)
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')
        try:
            bookings = Booking.objects.filter(
                booked_for=request.user).order_by('-booking_date')
            paginator = Paginator(bookings, 15)  # Show 15 bookings per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        except EmptyResultSet:
            messages.add_message(request, messages.INFO,
                                 'No bookings to display. Try later')
            HttpResponseRedirect('bookings/booking_detail.html')

        return render(
            request,
            "bookings/booking_detail.html",
            {
                "bookings": page_obj
            }
        )


class UpcomingBookingDetail(View):
    """ view upcoming booking details """

    def get(self, request, *args, **kwargs):

        """ View booking details selected """
        # check that user is logged in
        rights = check_access(request.user)
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')
        try:
            bookings = Booking.objects.filter(
                booked_for=request.user, booking_status='B',
                dinner_date__gte=datetime.now().date()).order_by('dinner_date')
            paginator = Paginator(bookings, 15)  # Show 15 bookings per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            if len(bookings) == 0:
                raise EmptyResultSet
        except EmptyResultSet:
            messages.add_message(request, messages.INFO,
                                 'No upcoming bookings, make a booking first')
            HttpResponseRedirect('bookings/up/upcoming_booking_detail.html')

        return render(
            request,
            "bookings/up/upcoming_booking_detail.html",
            {
                "bookings": page_obj
            }
        )


class BookForOthers(View):
    """ Make booking for another person """

    def get(self, request, *args, **kwargs):
        """ View user details to select first """

        # check that user is logged in
        rights = check_access(request.user, ("operator", ))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')

        users = User.objects.all().values(
                    'username', 'first_name', 'last_name',
                    'email').order_by('first_name')
        paginator = Paginator(users, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "bookings/others/book_for_others.html",
            {
                "users": page_obj
            }
        )

    def post(self, request, *args, **kwargs):
        """ The POST method filters the displayed records
            according to the clicked icon on the template
        """
        # check that user is operator
        rights = check_access(request.user, ("operator", ))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')

        # filter by username
        if request.POST.get('user_name'):
            user_name = request.POST.get('user_name').strip()
            users = User.objects.all().values(
                    'username', 'first_name', 'last_name',
                    'email').filter(username__icontains=user_name)
        # filter by email address
        elif request.POST.get('email'):
            email = request.POST.get('email').strip()
            users = User.objects.all().values(
                    'username', 'first_name', 'last_name',
                    'email').filter(email__icontains=email)
        else:
            users = User.objects.all().values(
                    'username', 'first_name', 'last_name',
                    'email').order_by('first_name')

        paginator = Paginator(users, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "bookings/others/book_for_others.html",
            {
                "users": page_obj,
            }
        )


class UpdateBookingStatus(View):
    """ Update the status after customer has been served
        This page enables display of bookings and filtering
        the displayed list """

    def get(self, request, *args, **kwargs):
        """ View booking details """
        # check that user is logged in
        rights = check_access(request.user, ("operator", "administrator"))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')
        request.session['Update_return'] = 'Select Booking'
        booking = query_booking(request, 'get', 'update_booking', 'B')
        # only current bookings
        paginator = Paginator(booking, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "bookings/update/update_booking.html",
            {
                "bookings": page_obj
            }
        )

    def post(self, request, *args, **kwargs):
        """filter booking details displayed """

        rights = check_access(request.user, ("operator", "administrator"))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')

        booking = query_booking(request, 'post', 'update_booking', 'B')

        paginator = Paginator(booking, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "bookings/update/update_booking.html",
            {
                "bookings": page_obj,
            }
        )


class BookingUpdateAction(View):
    """ booking update action
        When operator selects a booking to update
        the booking id is passed in and updated here
    """

    def get(self, request, booking_id, *args, **kwargs):
        """ Find the booking that was selected """

        rights = check_access(request.user, ("administrator", "operator"))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')

        return_to = request.session.get('Update_return')
        if not return_to:
            return_to = "Select Booking"

        booking = get_object_or_404(Booking, id=booking_id)
        form = UpdateBookingForm()
        return render(
            request,
            "bookings/update/update_booking_action.html",
            {
                "booking": booking,
                "form": form,
                "return_to": return_to
            }
        )

    def post(self, request, booking_id, *args, **kwargs):
        """ Update booking status details selected """

        rights = check_access(request.user, ("administrator", "operator"))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')
        return_to = request.session.get('Update_return')
        booking = get_object_or_404(Booking, id=booking_id)
        status = request.POST.get('booking_status')
        if len(status.strip()) != 0:
            status = get_object_or_404(BookingStatus, code=status)
        else:
            messages.add_message(request, messages.ERROR,
                                 'Please select a booking status first')
            return redirect('update_booking_action', booking_id)

        if booking.booking_status == status:
            messages.add_message(request, messages.ERROR,
                                 'Please select a different status')
            form = UpdateBookingForm
            return render(
                request,
                "bookings/update/update_booking_action.html",
                {
                    "booking": booking,
                    "form": form
                }
            )

        booking.booking_status = status
        booking.save()
        messages.add_message(request, messages.INFO,
                             'Booking updated successfully')
        bookings = Booking.objects.filter(booking_status=status)
        paginator = Paginator(bookings, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if return_to == "past_due_list":
            return redirect(return_to)
        else:
            return redirect('update_booking')


class BookingDetailsList(View):
    """ Query booking details list """

    def get(self, request, *args, **kwargs):

        """ View booking details """

        rights = check_access(request.user, ("administrator", "operator"))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')

        booking = query_booking(request, 'get','booking_details_list')
        paginator = Paginator(booking, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "bookings/blist/booking_list.html",
            {
                "bookings": page_obj
            }
        )

    def post(self, request, *args, **kwargs):
        """ Search the booking table based on user selected criteria
        First check dates and booking status together,
        then dates together
        followed by dates separately
        followed by username
        and finally booking status
        """
        rights = check_access(request.user, ("administrator", "operator"))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')

        booking = query_booking(request, 'post', "booking_details_list")
        paginator = Paginator(booking, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "bookings/blist/booking_list.html",
            {
                "bookings": page_obj,
            }
        )


class PastDueList(View):
    """ Past due booking details list """

    def get(self, request, *args, **kwargs):

        """ View past due booking details """

        rights = check_access(request.user, ("operator", ))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')

        # get the number of minutes past due
        # booking time to consider as no show
        no_show_min = get_object_or_404(SystemPreference, code="N")
        no_show = no_show_min.data

        today = datetime.now().date()
        booking = Booking.objects.filter(
            (Q(dinner_date__lt=today) |
              (Q(dinner_date=today) &
                Q(start_time__start_time__lte=(
                    datetime.now() - timedelta(minutes=no_show))))) & Q(
                        booking_status="B")).order_by('dinner_date')
        paginator = Paginator(booking, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "bookings/pastdue/past_due_list.html",
            {
                "bookings": page_obj
            }
        )

    def post(self, request, booking_id, *args, **kwargs):
        """ Put where the user is calling the update action into session
            This is to enable the user return to the proper invoking view
         """
        rights = check_access(request.user, ("administrator", "operator"))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')

        request.session['Update_return'] = 'past_due_list'
        return redirect('update_booking_action', int(booking_id))


class DeleteBooking(View):
    """ Delete booking list of eligible bookings
        Queries the database according to criteria
        entered by user
    """

    def get(self, request, *args, **kwargs):
        """ View booking details """

        rights = check_access(request.user, ("administrator", ))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')

        booking = query_booking(request, 'get', 'delete_booking', 'F')
        # only fulfilled bookings
        paginator = Paginator(booking, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "bookings/del/delete_booking.html",
            {
                "bookings": page_obj
            }
        )

    def post(self, request, *args, **kwargs):
        """ Retrieves list of bookings according to user entered criteria """

        rights = check_access(request.user, ("administrator", ))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')

        booking = query_booking(request, 'post', 'delete_booking', 'F')

        paginator = Paginator(booking, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "bookings/del/delete_booking.html",
            {
                "bookings": page_obj,
            }
        )


class DeleteUpdateAction(View):
    """ Methods to delete the selected booking """

    def get(self, request, booking_id, *args, **kwargs):
        """ Find and display the booking that was selected """

        rights = check_access(request.user, ("administrator", ))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')

        booking = Booking.objects.get(id=booking_id)
        form = UpdateBookingForm
        return render(
            request,
            "bookings/del/delete_booking_action.html",
            {
                "booking": booking,
                "form": form
            }
        )

    def post(self, request, booking_id, *args, **kwargs):
        """ Delete booking status details selected """

        rights = check_access(request.user, ("administrator", ))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')

        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        messages.add_message(request, messages.INFO,
                             'Booking deleted successfully')
        bookings = Booking.objects.filter(booking_status='F')
        paginator = Paginator(bookings, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "bookings/del/delete_booking.html",
            {
                "bookings": page_obj
            }
        )


class EditBooking(View):
    """ These methods enable the customer to edit the booking """

    def get(self, request, booking_id, *args, **kwargs):
        """ Display the booking form together with the
            booking details for editing
        """
        rights = check_access(request.user)
        if check_access(request.user) != "OK":
            messages.error(request, (rights))
            return redirect('/')

        price_queryset = get_object_or_404(SystemPreference, code="P")
        buffet_price = price_queryset.data
        booking = get_object_or_404(Booking, id=booking_id)
        cuisine_queryset = Cuisine.objects.all()
        form = BookingForm(instance=booking)

        return render(
            request,
            "bookings/edit/edit_booking.html",
            {
                "buffet_price": buffet_price,
                "form": form,
                "cuisines": cuisine_queryset,
                "booking_id": booking_id,
                "cuisine_choice": booking.cuisines
            }
        )

    def post(self, request, booking_id, *args, **kwargs):
        # check if user is logged in
        rights = check_access(request.user)
        if check_access(request.user) != "OK":
            messages.error(request, (rights))
            return redirect('/')

        booking_status = get_object_or_404(BookingStatus, code="B")
        booking_qs = BookingForm(data=request.POST)
        cuisine_choices = request.POST.getlist('cuisine_option')
        if len(cuisine_choices) == 0:
            messages.add_message(request, messages.WARNING,
                                 'Please select one or more cuisine\
                                      choices before proceeding')
            return redirect("edit_booking", booking_id)

        if booking_qs.is_valid():

            # fetch existing booking
            booking = get_object_or_404(Booking, id=booking_id)
            # check that dinner date is in future or today
            # if today check that time is in future
            dinner_date_str = request.POST.get('dinner_date')
            stime = request.POST.get('start_time')
            ans = is_dinner_date_in_future(dinner_date_str, stime)
            if ans['msg'] != "OK":
                messages.add_message(request, messages.WARNING, ans['msg'])
                return redirect('home')
            time_entered = ans['time_entered']

            try:

                user_to_book = request.user
                with transaction.atomic():
                    time_entered_qs = BuffetPeriod.objects.filter(
                        id=request.POST.get('start_time'))
                    time_entered = get_object_or_404(time_entered_qs)
                    # delete existing tables
                    TablesBooked.objects.filter(booking_id=booking_id).delete()

                    # check seats availability
                    tables = book_seats(int(request.POST.get('seats')),
                                        request.POST.get('dinner_date'),
                                        time_entered)
                    if len(tables) == 0:
                        # no seats found on selected date
                        messages.add_message(request, messages.WARNING,
                                             'So sorry, Graces Buffet is fully booked\
                        on your chosen date and time. Try another date/time.')
                        return redirect("edit_booking", booking.id)
                    else:

                        booking.booked_for = user_to_book
                        booking.booked_by = request.user
                        booking.booking_status = booking_status
                        booking.seats = request.POST.get('seats')
                        booking.dinner_date = request.POST.get('dinner_date')
                        booking.start_time = time_entered
                        booking.edited = True

                        # save tables booked
                        for table_item, seat in tables.items():
                            TablesBooked.objects.create(
                                booking_id=booking,
                                seats_booked=seat,
                                table_id=table_item,
                                time_booked=time_entered.start_time,
                                date_booked=booking.dinner_date,
                                table_capacity=table_item.total_seats)

                    # delete existing cuisine choices
                    CuisineChoice.objects.filter(
                        booking_id=booking_id).delete()

                    # save the cuisine choices
                    cuisines = ""
                    if len(cuisine_choices) > 0:
                        for choice in cuisine_choices:
                            cuisine_qs = Cuisine.objects.filter(id=choice)
                            cuisine_rec = get_object_or_404(cuisine_qs)
                            cuisines += cuisine_rec.name + ", "
                            CuisineChoice.objects.create(
                                booking_id=booking,
                                cuisine_id=cuisine_rec)
                            booking.cuisines = cuisines[:-2]
                    booking.save()
                    messages.add_message(request, messages.INFO,
                                         'Thank you: Your booking has\
                                          been confirmed.')
                    return HttpResponseRedirect(reverse('booking_confirm',
                                                args=[booking.id]))
            except IntegrityError:
                messages.add_message(request, messages.WARNING,
                                     'Your booking could not be completed now\
                                     check your entry and try again.')
                return redirect("edit_booking", booking_id)
        else:
            messages.add_message(request, messages.WARNING,
                                 'Your booking could not be completed now\
                                  check your entry and try again.')
            return redirect("edit_booking", booking_id)
