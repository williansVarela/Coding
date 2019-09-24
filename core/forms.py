from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from django import forms
from core.models import User
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs = {'id': 'login', 'class': 'fadeIn second', 'name': 'login',
                                                'placeholder': 'E-mail'}
        self.fields['password'].widget.attrs = {'id': 'password', 'class': 'fadeIn third', 'name': 'login',
                                                'placeholder': 'Senha'}


class UserCreateForm(UserCreationForm):

    error_messages = {
        'password_mismatch': _("Os dois campos de senha não são iguais."),
    }

    name = forms.CharField(label='Nome Completo', min_length=4, max_length=150)
    email = forms.EmailField(label='E-mail')
    date_of_birth = forms.DateField(label='Data de Nascimento')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs = {'class': 'form-control', 'placeholder': 'Digite o nome'}
        self.fields['email'].widget.attrs = {'class': 'form-control', 'placeholder': 'Digite a e-mail'}
        self.fields['date_of_birth'].widget.attrs = {'class': 'form-control', 'placeholder': 'Digite a data de nascimento'}
        self.fields['password1'].widget.attrs = {'class': 'form-control', 'placeholder': 'Digite a senha'}
        self.fields['password2'].widget.attrs = {'class': 'form-control', 'placeholder': 'Digite a senha novamente'}

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email já cadastrado")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("As senhas não correspondem")

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['name'],
            self.cleaned_data['email'],
            self.cleaned_data['date_of_birth'],
            self.cleaned_data['password1']
        )
        return user

    class Meta:
        model = User
        fields = ('name', 'email', 'date_of_birth', 'password1', 'password2',)


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



