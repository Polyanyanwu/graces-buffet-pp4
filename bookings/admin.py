""" Module for Admin to have access to some tables
    in the booking application
"""

from django.contrib import admin
from .models import Booking, TablesBooked, Notification


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    ''' Maintain booking list '''
    model = Booking
    list_filter = ('dinner_date', 'cuisines', 'booked_for')


@admin.register(TablesBooked)
class TablesBookedAdmin(admin.ModelAdmin):
    ''' Maintain tables booked list '''
    model = TablesBooked


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    ''' Maintain Notifications list '''
    model = Notification
    list_display = ('subject', 'notice_date', 'user', )
    search_fields = ['subject', 'message']
