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

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        self.fields['local'].widget.attrs = {'class': 'form-control', 'placeholder': 'Local do evento'}
        self.fields['local'].required = True
        self.fields['start_date'].widget.attrs = {'class': 'form-control', 'placeholder': 'DD/MM/AAAA'}
        self.fields['start_date'].required = True
        self.fields['end_date'].widget.attrs = {'class': 'form-control', 'placeholder': 'opcional'}
        self.fields['end_date'].required = False
        self.fields['schedule'].widget.attrs = {'class': 'form-control', 'placeholder': 'Ex: 15:30'}
        self.fields['schedule'].required = True
        self.fields['frequency'].widget.attrs = {'class': 'form-control'}
        self.fields['frequency'].required = True
        self.fields['type_event'].widget.attrs = {'class': 'form-control'}
        self.fields['type_event'].required = True

    class Meta:
        model = Event
        exclude = ('address',)


