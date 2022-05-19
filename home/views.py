""" home view for the home page, contact us, terms of use and privacy policy"""

from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
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
            user=user).order_by('-notice_date').values(
            'pk', 'subject', 'notice_date', 'message')

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


class NotificationDetail(View):
    """ view notifications """

    def get(self, request, notice_id, *args, **kwargs):

        """ View notification details selected """
        try:
            notice = Notification.objects.get(id=notice_id)
        except Exception:
            messages.add_message(request, messages.INFO,
                                 'Detailed display failed, try later')
            HttpResponseRedirect('home/notification_detail.html')

        return render(
            request,
            "home/notification_detail.html",
            {
                "notice": notice
            }
        )

    def post(self, request, notice_id, *args, **kwargs):
        """ Delete notification details selected """
        try:
            notice = Notification.objects.get(id=notice_id)
            notice.delete()
            notice_qs = Notification.objects.filter(
                user=request.user).order_by('-notice_date').values(
                'pk', 'subject', 'notice_date', 'message')
            messages.add_message(request, messages.INFO,
                                 'Notification deleted successfully')
        except Exception:
            messages.add_message(request, messages.INFO,
                                 'Deleted failed, try later')
            HttpResponseRedirect('home/notification_detail.html')

        return render(
            request,
            "home/get_notification.html",
            {
                "notifications": notice_qs
            }
        )
