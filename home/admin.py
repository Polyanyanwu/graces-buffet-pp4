""" Admin registration for contact us form """

from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ''' Maintain Contact messages list '''
    model = Contact
    list_display = ('date_time', 'subject', 'sender', 'message_body', 'user', )
    search_fields = ['subject', 'message_body']
    list_filter = ('subject', )
