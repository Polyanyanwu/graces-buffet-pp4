""" Cuisine Admin access """

from django.contrib import admin
from .models import Cuisine


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    ''' Maintain cuisine types '''
    model = Cuisine
    list_display = ('name', 'description', 'cuisine_image', 'created_on', )
    readonly_fields = ["created_on"]
