"""Utility to validate user access """

from .templatetags import user_belong_group


def check_access(request_user, group_name=None):
    """ Check if a user is authenticated and belongs to stated group
    IF no group is provided, just check that user is logged in

    Return:
      Message OK if authenticated or the error message
      """
    if request_user.is_authenticated:
        if group_name is None or user_belong_group.has_group(
                request_user, group_name):
            return "OK"
        else:
            return "Sorry you do not have access to this page"
    else:
        return "Login is required to access this page"
