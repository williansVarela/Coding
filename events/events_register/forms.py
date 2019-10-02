# -*- encoding:utf-8 -*-
from django import forms
from django.forms import ModelForm, Form
from events.models import Event
from contacts.contacts_register.models import Address
from contacts.contacts_register.forms import AddressForm


class AddressForm(AddressForm):
    class Meta:
        model = Address
        fields = '__all__'


class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ('address',)


