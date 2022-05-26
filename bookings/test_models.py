""" Testing of Booking Models """

from datetime import datetime
from django.test import TestCase
from django.core import mail
from django.contrib.auth.models import User
from general_tables.models import BookingStatus, BuffetPeriod
from .models import Notification, Booking


class TesItemForm(TestCase):
    """ Form testing class"""
    def setUp(self):
        User.objects.create(username="test", password='passwd',
                            email='poly@gmail.com')
        BuffetPeriod.objects.create(start_time=datetime.now().time())
        BookingStatus.objects.create(code='B', description='Booked')

    def test_notification_user_is_required(self):
        """ test notification user is required """
        with self.assertRaisesMessage(ValueError, 'Cannot assign'):
            Notification.objects.create(subject='Test Subject',
                                        message='Test message',
                                        notice_date=datetime.now(), user="")

    def test_booking_notice_is_sent(self):
        """ Test that Notification records is created
            and email is sent to user
        """
        user = User.objects.get(username='test')
        buffet_period = BuffetPeriod.objects.get(id=1)
        booking_status = BookingStatus.objects.get(code='B')
        Booking.objects.create(
            booked_for=user,
            start_time=buffet_period,
            booking_status=booking_status,
            booking_date=datetime.now(),
            seats=4
        )
        # Check notification record is created
        self.assertTrue(len(list(Notification.objects.all())) > 0)
        # Check confirmation email is sent
        self.assertEqual(mail.outbox[0].subject, 'Booking Confirmation')
