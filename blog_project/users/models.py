from django.db import models
from django.contrib.auth.models import User

# a packages pillow to handle the images
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# one to one relationship one user has one profile
# one profile has one user
# Create your models here.


class Profile(models.Model):
    # after the user is deleted, the profile will be deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # default.jpg : the default image for any user
    # when user upload a profile, the profile will be uploaded to profile_pics directory
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        # when the user pronoun the profile, will pronoun the user profile
        return f'{self.user.username} Profile'

    # when we save an instance of profile
    # the functions will run
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # open the image the current profile
        # we can resize the image the user wanna upload
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# any time when we make a change to model, we need to make database change
