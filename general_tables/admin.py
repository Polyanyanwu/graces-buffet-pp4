""" admin config and registration for general tables """

from django.contrib import admin
from .models import BookingStatus, BuffetPeriod


class BookingStatusAdmin(admin.ModelAdmin):
    ''' Maintain booking status list '''
    model = BookingStatus
    list_display = ('description', )


class BuffetPeriodsAdmin(admin.ModelAdmin):
    ''' Maintain booking status list '''
    model = BuffetPeriod
    list_display = ('time_seconds', )

    def time_seconds(self, obj):
        """ Format time properly """
        return obj.start_time.strftime("%H:%M")


# Models registration with relevant classes
admin.site.register(BookingStatus, BookingStatusAdmin)
admin.site.register(BuffetPeriod, BuffetPeriodsAdmin)
