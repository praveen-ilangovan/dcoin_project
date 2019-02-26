from django import forms
from django.contrib.auth.models import User

from .models import UserProfileModel

class UserRegistrationForm(forms.ModelForm):
    """ admin User form

    """
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileRegistrationForm(forms.ModelForm):
    """ Extend the User model form

    """
    class Meta:
        model = UserProfileModel
        fields = ('profile_pic',)
