""" Urls settings for the home application """

from django.urls import path
from . import views


urlpatterns = [
    # root url
    path('', views.index, name='home'),
]
