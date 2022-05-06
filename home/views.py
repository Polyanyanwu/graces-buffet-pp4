""" home view for the home page, contact us, terms of use and privacy policy"""

from django.shortcuts import render


def index(request):
    """ A view to return the main index page """

    template = 'home/index.html'
    context = {
        'home_page': True,
    }
    return render(request, template, context)
