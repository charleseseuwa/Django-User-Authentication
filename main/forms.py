from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm    #form for creating the instance
from django import forms


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text="Please provide a valid email address")
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2" ]