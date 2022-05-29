""" URLs for cuisine application """

from django.urls import path
from . import views


urlpatterns = [
     path('', views.CuisineSummary.as_view(),
          name='cuisine_summary'),
]
