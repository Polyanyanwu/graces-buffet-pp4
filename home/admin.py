from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ''' Maintain Contact messages list '''
    model = Contact
    list_display = ('date_time', 'subject', 'sender','message_body', 'user', )