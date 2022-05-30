""" admin config and registration for general tables
    The summernote library was used to enable the superuser
    to input and maintain the Terms of Use and Privacy Notice
    for the site instead of hard coding it"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    BookingStatus, BuffetPeriod, DiningTable, HomeMessage)


@admin.register(BookingStatus)
class BookingStatusAdmin(admin.ModelAdmin):
    ''' Maintain booking status list '''
    model = BookingStatus
    list_display = ('code', 'description', )

    def get_actions(self, request):
        """ Disable delete action from Booking status as it is critical
            to system function. Admin can change the description only
        """
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        """ Remove Delete button from everyone """
        return False


@admin.register(BuffetPeriod)
class BuffetPeriodsAdmin(admin.ModelAdmin):
    ''' Maintain booking status list '''
    model = BuffetPeriod
    list_display = ('time_seconds', )

    def time_seconds(self, obj):
        """ Format time properly """
        return obj.start_time.strftime("%H:%M")


@admin.register(DiningTable)
class DiningTableAdmin(admin.ModelAdmin):
    ''' Maintain dining tables '''
    model = DiningTable
    list_display = ('location', 'description', 'total_seats', 'used_seats', )


@admin.register(HomeMessage)
class HomeMessageAdmin(SummernoteModelAdmin):
    """ Maintain Text for Privacy policy & Terms of Use"""
    list_display = ('code', )
    summernote_fields = ('description')
