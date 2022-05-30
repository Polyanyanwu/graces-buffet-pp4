""" template tag for user group """

from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    """ Template tag used to check the group that user belongs to
        at the NAV bar to display the correct menus
    """
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False
