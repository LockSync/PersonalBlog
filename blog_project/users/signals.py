from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# the meaning of signals.py : every time a user is created, the user automatically get the profile
# if we don't use the signal , every time a new user ins created ,we have to go the admin page and set the default pics
# to the user manually


# when a user is saved , then send the signal(post_save)
# and the signal will be received by the receiver
# the receiver is the create_profile function
# and the function takes all the parameters that the post_save passes to it
# and one of those is the instance of the User
# if the user was created,then create a profile object with a user equals to
# the instance of user that was created
# the created_profile function runs every time the user object gets created


@receiver(post_save, sender=User)
def created_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# save the profile every time user object gets saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
