''' Urls for the cancel booking app '''

from django.urls import path
from . import views


urlpatterns = [
    path('cancel_booking/<username>', views.CancelMyBooking.as_view(),
         name='cancel_my_booking'),
    path('cancel_booking/', views.CancelOtherBooking.as_view(),
         name='cancel_other_booking'),
]
