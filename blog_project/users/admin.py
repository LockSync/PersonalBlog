from django.contrib import admin
from .models import Profile

# register the Profile model in User app
admin.site.register(Profile)
