""" Cancel bookings module """

from datetime import datetime
from django.shortcuts import render

# from django.shortcuts import get_object_or_404
from django.views import View
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages

from general_tables.models import BookingStatus
from bookings.models import Booking


class CancelMyBooking(View):
    """ Cancel booking for self """

    def get(self, request, username, *args, **kwargs):

        """ View booking details """
        try:
            user_to_cancel = User.objects.get(username=username)
            bookings = Booking.objects.filter(
                booked_for=user_to_cancel, booking_status='B',
                dinner_date__gte=datetime.now()).order_by('-booking_date')
            paginator = Paginator(bookings, 15)  # B is currently booked
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        except Exception:
            messages.add_message(request, messages.INFO,
                                 'Detailed display of bookings\
                                  failed, try later')
            HttpResponseRedirect('cancel_booking/cancel_my_booking.html')

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
        page_obj = None
        try:
            booking_id = request.POST.get('booking_id')

            booking = Booking.objects.get(id=booking_id)
            booking_status = BookingStatus.objects.get(code='C')
            booking.booking_status = booking_status
            booking.cancelled_by = request.user
            booking.date_cancelled = timezone.now().date()
            booking.save()
            bookings = Booking.objects.filter(
                booked_for=request.user, booking_status='B',
                dinner_date__gte=datetime.now()).order_by('-booking_date')
            paginator = Paginator(bookings, 15)  # B is currently booked
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            messages.add_message(request, messages.INFO,
                                 'Booking has been cancelled successfully')
        except Exception as excpt_m:
            print(excpt_m)
            messages.add_message(request, messages.INFO,
                                 'Cancellation failed, try later')
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
        try:

            users = User.objects.all().values(
                     'username', 'first_name', 'last_name',
                     'email').order_by('first_name')
            paginator = Paginator(users, 10)  # B is currently booked
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        except Exception:
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

            paginator = Paginator(users, 10)  # B is currently booked
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        except Exception:
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
