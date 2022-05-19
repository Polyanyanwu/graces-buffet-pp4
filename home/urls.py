""" Urls settings for the home application """

from django.urls import path
from . import views


urlpatterns = [
    path('notice/', views.ViewNotification.as_view(), name='get_notification'),
]
