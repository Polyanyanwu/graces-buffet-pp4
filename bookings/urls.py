''' Urls for the booking app '''

from django.urls import path
from . import views


urlpatterns = [
    path('', views.MakeBookings.as_view(), name='home'),
]
