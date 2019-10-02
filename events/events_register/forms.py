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
        self.fields['start_date'].widget.attrs = {'class': 'form-control', 'placeholder': '29/06/2019'}
        self.fields['end_date'].widget.attrs = {'class': 'form-control', 'placeholder': '9/11/2019'}
        self.fields['schedule'].widget.attrs = {'class': 'form-control', 'placeholder': '15h00'}
        self.fields['frequency'].widget.attrs = {'class': 'form-control'}
        self.fields['type_event'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Event
        exclude = ('address',)


