""" Test booking views """
from datetime import datetime
from django.test import TestCase, RequestFactory, Client
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.auth.models import Group
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
        # Needed because template tags on the base looks for the two groups
        Group.objects.create(name='operator')
        Group.objects.create(name='administrator')

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
        response = MakeBookings.as_view()(request)
        response.client = Client()
        assert response.status_code == 200

    def test_cuisine_choice_is_required(self):
        """ When authenticated user signs in
            test that cuisine choice is required """
        buffet_period = BuffetPeriod.objects.get(id=1)
        dinner_date = datetime.strptime('2022-08-21', "%Y-%m-%d").date()
        request = self.factory.post(
            '/', {'booking_date': datetime.now(),
                  'dinner_date': dinner_date,
                  'seats': 3, 'start_time': buffet_period.id,
                  'cuisine_option': []})

        request.user = self.user
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = MakeBookings.as_view()(request)
        response.client = Client()

        # if cuisine choice is not selected user is redirected
        # to booking page at home, but if booking succeeded user is redirected
        # to confirmation page
        assert response.status_code == 200
