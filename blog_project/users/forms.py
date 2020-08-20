from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.models import Profile


# all the class will be used in views.py
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    #  keeps the config in one place
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# update the username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# update the image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
