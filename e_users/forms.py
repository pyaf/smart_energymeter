from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class UserAuthForm(AuthenticationForm):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(attrs={'class': 'validate',
                                                             'name': 'username'}))
    password = forms.CharField(label="Password",
                               widget=forms.TextInput(attrs={'class': 'validate',
                                                             'type':'password',
                                                             'name': 'password'}))
