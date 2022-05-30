""" Query the database and produce summary of Cuisines for a given date """

from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.db.models import Count
from cuisine.models import CuisineChoice
from user_account.user_auth import check_access
from bookings.forms import BookingForm


class CuisineSummary(View):
    """ Cuisine summary page """

    def get(self, request, *args, **kwargs):
        """ Load initial summary with data for current date """
        # check that user is operator or administrator
        rights = check_access(request.user, ("operator", "administrator"))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')

        form = BookingForm()

        cuisines = CuisineChoice.objects.filter(
            booking_id__dinner_date=datetime.now().date()).values(
            'booking_id__dinner_date', 'cuisine_id__name').order_by(
            'cuisine_id').annotate(total_cuisine=Count('cuisine_id'))

        return render(
            request,
            "cuisine/cuisine_summary.html",
            {
                "form": form,
                "cuisines": cuisines
            }
        )

    def post(self, request, *args, **kwargs):
        # Get the dinner date entered by user and 
        # use it to get summary of each buffet type for that day

        # check that user is operator or administrator
        rights = check_access(request.user, ("operator", "administrator"))
        if rights != "OK":
            messages.error(request, (rights))
            return redirect('/')
        form = BookingForm(request.POST or None)
        dinner_date = request.POST.get('dinner_date')
        cuisines = CuisineChoice.objects.filter(
            booking_id__dinner_date=dinner_date).values(
            'booking_id__dinner_date', 'cuisine_id__name').order_by(
            'cuisine_id').annotate(total_cuisine=Count('cuisine_id'))

        return render(
            request,
            "cuisine/cuisine_summary.html",
            {
                "form": form,
                "cuisines": cuisines
            }
        )
