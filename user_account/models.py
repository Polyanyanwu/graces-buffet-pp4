""" User profile model """

from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """ additional data for the user """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, blank=True)
    special_request = models.TextField(blank=True)

    def __str__(self):
        ''' String method to return the username '''
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ After a new user is created, create a profile record too """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """ When user is amended save the profile too """
    instance.profile.save()


class UserGroup(models.Model):
    """ Used to enable select group for updating user group """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group_name = models.OneToOneField(Group, on_delete=models.CASCADE)

    def __str__(self):
        ''' String method to return the group '''
        return self.group_name.name
