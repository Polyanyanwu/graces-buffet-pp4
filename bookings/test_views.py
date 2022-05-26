""" Test booking views """
from datetime import datetime
from django.test import TestCase, RequestFactory, Client
from django.contrib.messages.storage.fallback import FallbackStorage
from django.shortcuts import reverse
from django.contrib.auth.models import User, AnonymousUser
from general_tables.models import SystemPreference, BookingStatus, BuffetPeriod
from cuisine.models import Cuisine
from .views import MakeBookings


class TestViews(TestCase):
    """ test views """

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username='testuser',
                                        email='poly@gmail.com',
                                        password='passwd')
        SystemPreference.objects.create(code="M", data='8')
        SystemPreference.objects.create(code="P", data='45')
        BookingStatus.objects.create(code='B', description="Booked")
        BuffetPeriod.objects.create(start_time=datetime.now().time())
        Cuisine.objects.create(name='Nigerian Cuisine',
                               description="Nigerian Cuisine")

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
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        request.user = AnonymousUser()
        response = MakeBookings.as_view()(request, f"{self.user.username}")
        response.client = Client()
        self.assertRedirects(response, reverse("home"))

    def test_cuisine_choice_is_required(self):
        """ When authenticated user signs in
            test that cuisine choice is required """
        buffet_period = BuffetPeriod.objects.get(id=1)
        request = self.factory.post('/testuser', {'booking_date':
                                    datetime.now(),
                                    'dinner_date': datetime.now().date(),
                                    'seats': 3, 'start_time': buffet_period.id,
                                    'cuisine_option': []})
        request.user = self.user

        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = MakeBookings.as_view()(request, f"{self.user.username}")
        response.client = Client()
        # if cuisine choice is not selected user is redirected
        # to booking page at home
        self.assertRedirects(response, reverse("home"))
