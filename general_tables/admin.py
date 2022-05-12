""" admin config and registration for general tables """

from django.contrib import admin
from .models import BookingStatus


class BookingStatusAdmin(admin.ModelAdmin):
    ''' Maintain booking status list '''
    model = BookingStatus
    list_display = ('status', )


# Models registration with relevant classes
admin.site.register(BookingStatus, BookingStatusAdmin)
