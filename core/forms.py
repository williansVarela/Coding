from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserChangeForm, PasswordChangeForm
from django.forms import ModelForm, Form
from django import forms
from core.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs = {'id': 'login', 'class': 'fadeIn second', 'name': 'login',
                                                'placeholder': 'E-mail'}
        self.fields['password'].widget.attrs = {'id': 'password', 'class': 'fadeIn third', 'name': 'login',
                                                'placeholder': 'Senha'}


class UpdatePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs = {'id': 'id_old_password', 'class': 'form-control', 'placeholder': 'Digite a senha'}
        self.fields['new_password1'].widget.attrs = {'id': 'id_new_password1', 'class': 'form-control', 'placeholder': 'Digite a nova senha'}
        self.fields['new_password2'].widget.attrs = {'id': 'id_new_password2', 'class': 'form-control', 'placeholder': 'Confirme a nova senha'}


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'date_of_birth',
        )



