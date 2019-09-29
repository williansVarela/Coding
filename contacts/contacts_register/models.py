# -*- encoding:utf-8 -*-
from django.db import models
from core.helpers.states import STATE_CHOICES
from django.db.models.fields import CharField
from contacts.contacts_register import validators
from django.utils.translation import gettext_lazy as _


class StateField(CharField):
    """A model field for states of Brazil."""

    description = _("Estados do Brasil (duas letras em maiusculo).")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 2
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs


class ZipCodeField(CharField):
    """
    A model field for the brazilian zip code
    """

    description = _("CEP")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 9
        super().__init__(*args, **kwargs)
        self.validators.append(validators.ZipCodeValidator())


class PhoneField(CharField):
    """
    A model field for the brazilian phone
    """

    description = _("Telefone")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 13
        super().__init__(*args, **kwargs)
        self.validators.append(validators.PhoneValidator())


class Address(models.Model):
    zipcode = ZipCodeField(null=True, verbose_name='CEP')
    address = models.CharField(max_length=100, null=True, verbose_name='Endereço')
    number = models.CharField(max_length=5, null=True, verbose_name='Número')
    complement = models.CharField(max_length=25, null=True, verbose_name='Complemento')
    district = models.CharField(max_length=50, null=True, verbose_name='Bairro')
    city = models.CharField(max_length=50, null=True, verbose_name='Município')
    state = StateField(default='SP', null=True, verbose_name='Estado')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address

    class Meta:
        app_label = 'contacts'


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome Completo')
    email = models.EmailField(max_length=255, verbose_name='E-mail')
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.DO_NOTHING)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'contacts'


class Contact(models.Model):
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    phone = PhoneField(null=True, verbose_name='Telefone')
    _IS_ADOPTER_CHOICES = ((False, "Não"), (True, "Sim"))
    is_adopter = models.BooleanField(default=False, choices=_IS_ADOPTER_CHOICES, verbose_name='Adotou animal?')
    _TYPE_CHOICES = (('volunteer', "Voluntário"), ('donor', "Doador"), ('vet', "Veterinário"), ('partner', "Parceiro"))
    type = models.CharField(max_length=12, null=True, blank=True, choices=_TYPE_CHOICES, verbose_name='Tipo de contato')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.person.name

    class Meta:
        app_label = 'contacts'
        permissions = (("access_contact", "Acessar Contatos"),)
