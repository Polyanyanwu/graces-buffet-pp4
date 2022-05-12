""" admin config and registration for general tables """

from django.contrib import admin
from .models import BookingStatus, BuffetPeriod, SystemPreference, DiningTable


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


class SystemPreferenceAdmin(admin.ModelAdmin):
    ''' Maintain System Preferences list '''
    model = SystemPreference
    list_display = ('code', 'data', )


@admin.register(DiningTable)
class DiningTableAdmin(admin.ModelAdmin):
    ''' Maintain dining tables '''
    model = DiningTable
    list_display = ('location', 'description', 'total_seats', 'used_seats', )


# Models registration with relevant classes
admin.site.register(BookingStatus, BookingStatusAdmin)
# admin.site.register(BuffetPeriod, BuffetPeriodsAdmin)
admin.site.register(SystemPreference, SystemPreferenceAdmin)
