""" Override the ready method to enable signals to work """

from django.apps import AppConfig


class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'

    def ready(self):
        """
        Override the ready method and import signals
        """
        import bookings.signals
