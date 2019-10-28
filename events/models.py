# -*- encoding:utf-8 -*-
from django.db import models
from django.db.models.fields import CharField
from contacts.contacts_register.models import Address
from django.utils.translation import gettext_lazy as _
from core import validators


class ScheduleField(CharField):
    """
    A model field for hour schedule
    """
    description = _("Horário")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 5
        super().__init__(*args, **kwargs)
        self.validators.append(validators.ScheduleValidator())


class Event(models.Model):
    local = models.CharField(max_length=100, null=True, verbose_name='Local')
    start_date = models.DateField(null=True, blank=True, verbose_name='Data de início')
    end_date = models.DateField(null=True, blank=True, verbose_name='Data de termino')
    schedule = models.CharField(max_length=5, verbose_name='Horário')
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    _FREQUENCY_CHOICES = (('diário', "Diário"), ('semanal', "Semanal"), ('mensal', "Mensal"), ('anual', "Anual"), ('único', "Único"),)
    frequency = models.CharField(max_length=30, default='adoção', null=True, blank=True, choices=_FREQUENCY_CHOICES, verbose_name='Frequência')
    _TYPE_EVENT_CHOICES = (('adoção', "Adoção"),('outros', "Outros"),)
    type_event = models.CharField(max_length=30, default='adoção', null=True, blank=True, choices=_TYPE_EVENT_CHOICES, verbose_name='Tipo de evento')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.local

    class Meta:
        app_label = 'events'
        permissions = (("access_adoption_event", "Acessar Eventos de adoção"),)

