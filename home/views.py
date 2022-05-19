""" home view for the home page, contact us, terms of use and privacy policy"""

from django.shortcuts import render, get_object_or_404
from django.views import View
# from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from bookings.models import Notification


def index(request):
    """ A view to return the main index page """

    template = 'home/index.html'
    context = {
        'home_page': True,
    }
    return render(request, template, context)


class ViewNotification(View):
    """ view notifications """

    def get(self, request, *args, **kwargs):

        """ View notifications of the signed in user """

        if not request.user.is_authenticated:
            messages.add_message(request,
                                 messages.ERROR,
                                 'Please login first before you can access \
                                  Notifications. Click the Signup button above\
                                  or login if you already have an account ')
            return HttpResponseRedirect("/")
        user = request.user
        notice_qs = Notification.objects.filter(
            user=user).order_by('-notice_date')
        print("notice==", notice_qs)
        if len(notice_qs) == 0:
            messages.add_message(request, messages.ERROR,
                                 'No notifications for you yet. \
                                  Make a booking first before you receive \
                                  notifications.')

        return render(
            request,
            "home/get_notification.html",
            {
                "notifications": notice_qs
            }
        )
