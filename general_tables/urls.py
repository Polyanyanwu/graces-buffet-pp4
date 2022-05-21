""" URLs for general parameter table maintenance """
from django.urls import path
from . import views


urlpatterns = [
    path('sys_pref/', views.SystemPreferenceView.as_view(), name='system_preference'),
]
