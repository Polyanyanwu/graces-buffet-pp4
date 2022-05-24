""" Apps config for home app and to override the ready method
    to enable use of signals
"""
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """ default config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        """
        Override the ready method and import signals
        """
        import home.signals
