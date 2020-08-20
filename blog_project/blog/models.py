from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now())
    # if a user is deleted , the text will be deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # reverse : the full path as a string
        # after the user create a new post, and the page will go to the post
        return reverse('post-detail', kwargs={'pk': self.pk})
