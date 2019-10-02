# -*- encoding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from contacts.contacts_register.models import Address
from events.events_register.forms import AddressForm, EventForm
from events.models import Event
from django.contrib import messages
from django.shortcuts import render, redirect


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = 'login/'
    template_name = 'events/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['pagina'] = 'Eventos'
        context['page_title'] = 'Animais | Eventos'
        context['animals_active'] = 'active'
        context['confirm_modal'] = 'modal_confirm.html'
        context['object_model'] = 'evento'
        context['title_model'] = 'Remover Evento'
        context['url_modal'] = 'events:delete_event'
        context['events'] = Event.objects.select_related()

        return context

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)
