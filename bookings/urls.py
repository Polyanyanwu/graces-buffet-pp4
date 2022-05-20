''' Urls for the booking app '''

from django.urls import path
from . import views


urlpatterns = [
    path('', views.MakeBookings.as_view(), name='home'),
    path('<username>', views.MakeBookings.as_view(), name='other_home'),
    path('bookings/<booking_id>',
         views.DisplayBookingConfirm.as_view(),
         name='booking_confirm'),
    path('bookings/', views.BookingDetail.as_view(),
         name='booking_detail'),
    path('bookings/up/', views.UpcomingBookingDetail.as_view(),
         name='upcoming_booking_detail'),
    path('bookings/others/', views.BookForOthers.as_view(),
         name='book_for_others'),
]
