# -*- encoding:utf-8 -*-
from django import forms
from django.forms import ModelForm, Form
from contacts.contacts_register.models import Contact, Person, Address


class AddressForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)

        self.fields['zipcode'].widget.attrs = {'class': 'form-control', 'placeholder': '12345-123'}
        self.fields['zipcode'].required = False
        self.fields['address'].widget.attrs = {'class': 'form-control', 'placeholder': 'Endereço'}
        self.fields['address'].required = False
        self.fields['number'].widget.attrs = {'class': 'form-control', 'placeholder': '273'}
        self.fields['number'].required = False
        self.fields['complement'].widget.attrs = {'class': 'form-control', 'placeholder': 'Ex.: AP 125 BL A'}
        self.fields['complement'].required = False
        self.fields['district'].widget.attrs = {'class': 'form-control', 'placeholder': 'Digite o bairro'}
        self.fields['district'].required = False
        self.fields['state'].widget.attrs = {'class': 'form-control'}
        self.fields['state'].required = False
        self.fields['city'].widget.attrs = {'class': 'form-control', 'placeholder': 'Digite o município',
                                            'required': False}
        self.fields['city'].required = False

    class Meta:
        model = Address
        fields = '__all__'


class PersonForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs = {'class': 'form-control', 'placeholder': 'Digite o nome'}
        self.fields['email'].widget.attrs = {'class': 'form-control', 'placeholder': 'nome@exemplo.com'}

    class Meta:
        model = Person
        exclude = ('address',)


class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['phone'].widget.attrs = {'class': 'form-control', 'placeholder': 'xx-xxxx-xxxx'}
        self.fields['is_adopter'].widget.attrs = {'class': 'form-control'}
        self.fields['type'].widget.attrs = {'class': 'form-control'}
        self.fields['type'].required = True

    class Meta:
        model = Contact
        exclude = ('person',)
