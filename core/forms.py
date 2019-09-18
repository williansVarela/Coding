
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, Form
from django import forms

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs = {'id': 'login', 'class': 'fadeIn second', 'name': 'login', 'placeholder': 'E-mail'}
        self.fields['password'].widget.attrs = {'id': 'password', 'class': 'fadeIn third', 'name': 'login', 'placeholder': 'Senha'}