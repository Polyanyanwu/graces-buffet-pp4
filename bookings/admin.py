from django.contrib import admin

# Register your models here.
from .models import Booking, TablesBooked


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    ''' Maintain booking status list '''
    model = Booking


@admin.register(TablesBooked)
class TablesBookedAdmin(admin.ModelAdmin):
    ''' Maintain tables booked list '''
    model = TablesBooked
