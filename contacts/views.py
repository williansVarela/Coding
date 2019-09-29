# -*- encoding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from contacts.contacts_register.models import Contact


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = 'login/'
    template_name = 'contacts/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['pagina'] = 'Contatos'
        context['page_title'] = 'Contatos | Lista'
        context['contacts_active'] = 'active'
        context['confirm_modal'] = 'modal_confirm.html'
        context['object_model'] = 'contato'
        context['title_model'] = 'Remover Contato'
        context['url_modal'] = 'contacts:delete_contact'
        context['contacts'] = Contact.objects.select_related()


        return context

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


