""" Test booking views """
from django.test import TestCase, RequestFactory
from django.contrib.messages.api import MessageFailure
from django.contrib import messages
from django.contrib.auth.models import User, AnonymousUser
from django.test import Client
from .models import Booking
from .views import MakeBookings
from general_tables.models import SystemPreference


class TestViews(TestCase):
    """ test views """

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username='testuser',
                                        email='poly@gmail.com',
                                        password='passwd')
        SystemPreference.objects.create(code="M", data='8')
        SystemPreference.objects.create(code="P", data='45')

    def test_booking_home_page(self):
        """ test that home page responds """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/make_booking.html')

    def test_anonymous_user_disallowed_to_save_booking(self):
        """ Anonymous user cannot save booking
            A failure message is displayed and user
            redirected to home page"""
        request = self.factory.post('/testuser')
        # request.user = self.user
        request.user = AnonymousUser()
        try:
            response = MakeBookings.as_view()(request, f"{self.user.username}")
        except MessageFailure as msg:
            self.assertTrue('You cannot add messages without installing'
                            in str(msg))
