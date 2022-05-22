''' Urls for the booking app '''

from django.urls import path
from . import views


urlpatterns = [
     path('', views.MakeBookings.as_view(), name='home'),
     path('<username>', views.MakeBookings.as_view(), name='home'),
     path('bookings/<booking_id>',
          views.DisplayBookingConfirm.as_view(),
          name='booking_confirm'),
     path('bookings/', views.BookingDetail.as_view(),
          name='booking_detail'),
     path('bookings/up/', views.UpcomingBookingDetail.as_view(),
          name='upcoming_booking_detail'),
     path('bookings/others/', views.BookForOthers.as_view(),
          name='book_for_others'),
     path('bookings/update/', views.UpdateBookingStatus.as_view(),
          name='update_booking'),
     path('bookings/update/<booking_id>', views.BookingUpdateAction.as_view(),
          name='update_booking_action'),
     path('bookings/blist/', views.BookingDetailsList.as_view(),
          name='booking_details_list'),
     path('bookings/pastdue/', views.PastDueList.as_view(),
          name='past_due_list'),
     path('bookings/del/', views.DeleteBooking.as_view(),
          name='delete_booking'),
     path('bookings/del/<booking_id>', views.DeleteUpdateAction.as_view(),
          name='delete_booking_action'),
]
