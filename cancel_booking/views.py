""" Cancel bookings module """

from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.db.utils import DataError
from django.views import View
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from user_account.user_auth import check_access
from general_tables.models import BookingStatus
from bookings.models import Booking


class CancelMyBooking(View):
    """ Cancel booking for self """

    def get(self, request, username, *args, **kwargs):
        """ View booking details requires user is logged in"""
        rights = check_access(request.user)
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')

        user_to_cancel = get_object_or_404(User, username=username)

        bookings = Booking.objects.filter(
            booked_for=user_to_cancel, booking_status='B',
            dinner_date__gte=datetime.now().date()).order_by('-booking_date')
        paginator = Paginator(bookings, 15)  # B is currently booked
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "cancel_booking/cancel_my_booking.html",
            {
                "bookings": page_obj,
                "user_to_cancel": user_to_cancel.get_full_name()
            }
        )

    def post(self, request, username, *args, **kwargs):
        """ cancel selected booking """
        rights = check_access(request.user)
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')
        page_obj = None

        booking_id = request.POST.get('booking_id')
        booking = get_object_or_404(Booking, id=booking_id)
        booking_status = get_object_or_404(BookingStatus, code='C')
        booking.booking_status = booking_status
        booking.cancelled_by = request.user
        booking.date_cancelled = timezone.now().date()
        try:
            booking.save()
            messages.add_message(request, messages.INFO,
                                 'Booking has been cancelled successfully')
        except DataError:
            print(" Data error saving booking cancellation ")
            messages.add_message(request, messages.INFO,
                                 'Error saving cancellation, try later')
        # status B is currently booked
        bookings = Booking.objects.filter(
            booked_for=request.user, booking_status='B',
            dinner_date__gte=datetime.now().date()).order_by('-booking_date')
        paginator = Paginator(bookings, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # check if the cancellation is invoked from the up coming booking
        if 'up_coming_booking' in request.POST:
            return redirect('upcoming_booking_detail')
        else:
            HttpResponseRedirect('cancel_booking/notification_detail.html')

        return render(
            request,
            "cancel_booking/cancel_my_booking.html",
            {
                "bookings": page_obj
            }
        )


class CancelOtherBooking(View):
    """ Cancel booking for another person """

    def get(self, request, *args, **kwargs):

        """ View user details """
        # check that user is logged in and has access
        rights = check_access(request.user, ("operator", "administrator"))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')
        try:
            users = User.objects.all().values(
                     'username', 'first_name', 'last_name',
                     'email').order_by('first_name')
            paginator = Paginator(users, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        except DataError:
            messages.add_message(request, messages.INFO,
                                 'Detailed display of users\
                                  failed, try later')
            HttpResponseRedirect('cancel_booking/cancel_other_booking.html')

        return render(
            request,
            "cancel_booking/cancel_other_booking.html",
            {
                "users": page_obj
            }
        )

    def post(self, request, *args, **kwargs):
        """ Query the database to return list of users
            as given in the criteria inputted
        """
        # check that user is logged in and has access
        rights = check_access(request.user, ("operator", "administrator"))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')
        try:
            if request.POST.get('user_name'):
                user_name = request.POST.get('user_name').strip()
                users = User.objects.all().values(
                        'username', 'first_name', 'last_name',
                        'email').filter(username__icontains=user_name)
            elif request.POST.get('email'):
                email = request.POST.get('email').strip()
                users = User.objects.all().values(
                        'username', 'first_name', 'last_name',
                        'email').filter(email__icontains=email)
            else:
                users = User.objects.all().values(
                        'username', 'first_name', 'last_name',
                        'email').order_by('first_name')

            paginator = Paginator(users, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        except DataError():
            messages.add_message(request, messages.INFO,
                                 'Detailed display of users\
                                  failed, try later')
            HttpResponseRedirect('cancel_booking/cancel_other_booking.html')

        return render(
            request,
            "cancel_booking/cancel_other_booking.html",
            {
                "users": page_obj
            }
        )
