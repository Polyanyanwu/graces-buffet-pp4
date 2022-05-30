""" Module for Admin to have access to some tables
    in the booking application
"""

from django.contrib import admin
from .models import Booking, TablesBooked, Notification


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    ''' Maintain booking list '''
    model = Booking
    list_filter = ('booking_status', 'cuisines')
    list_display = ('booked_for', 'dinner_date', 'cuisines', 'booking_status')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    ''' Maintain Notifications list '''
    model = Notification
    list_display = ('subject', 'notice_date', 'user', )
    search_fields = ['subject', 'message']


@admin.register(TablesBooked)
class TablesBookedAdmin(admin.ModelAdmin):
    ''' Maintain Notifications list '''
    model = TablesBooked
    list_display = ('booking_id', 'table_id', 'table_capacity',
                    'seats_booked', 'date_booked', 'time_booked')
    ordering = ('-date_booked', 'booking_id')

    def get_actions(self, request):
        """ Disable delete action from Tables booked.
            Included here for report only
        """
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        """ Remove Delete button from everyone """
        return False

    def has_add_permission(self, request, obj=None):
        """ Remove add button """
        return False
