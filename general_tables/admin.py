""" admin config and registration for general tables """

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    BookingStatus, BuffetPeriod, SystemPreference, DiningTable, HomeMessage)


@admin.register(BookingStatus)
class BookingStatusAdmin(admin.ModelAdmin):
    ''' Maintain booking status list '''
    model = BookingStatus
    list_display = ('code', 'description', )


@admin.register(BuffetPeriod)
class BuffetPeriodsAdmin(admin.ModelAdmin):
    ''' Maintain booking status list '''
    model = BuffetPeriod
    list_display = ('time_seconds', )

    def time_seconds(self, obj):
        """ Format time properly """
        return obj.start_time.strftime("%H:%M")


@admin.register(SystemPreference)
class SystemPreferenceAdmin(admin.ModelAdmin):
    ''' Maintain System Preferences list '''
    model = SystemPreference
    list_display = ('code', 'data', )


@admin.register(DiningTable)
class DiningTableAdmin(admin.ModelAdmin):
    ''' Maintain dining tables '''
    model = DiningTable
    list_display = ('location', 'description', 'total_seats', 'used_seats', )


@admin.register(HomeMessage)
class HomeMessageAdmin(SummernoteModelAdmin):
    """ Maintain Text for Privacy policy & Terms of Use"""
    list_display = ('code', 'description', )
    summernote_fields = ('description')
