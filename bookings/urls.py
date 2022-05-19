''' Urls for the booking app '''

from django.urls import path
from . import views


urlpatterns = [
    path('', views.MakeBookings.as_view(), name='home'),
    path('bookings/<booking_id>',
         views.DisplayBookingConfirm.as_view(),
         name='booking_confirm'),
    path('bookings/',
         views.BookingDetail.as_view(),
         name='booking_detail'),
]
