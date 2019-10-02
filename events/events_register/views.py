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


@login_required
def register_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        address_form = AddressForm(request.POST)
        if event_form.is_valid() and address_form.is_valid():
            address = address_form.save()
            event = event_form.save(commit=False)
            event.address = address
            event.save()

            messages.success(request, 'Evento adicionado com sucesso!', extra_tags='alert alert-success alert-dismissible fade show')

            return redirect('events:home')
        
    else:
        address_form = AddressForm()
        event_form = EventForm()

    context = {'pagina': 'Eventos', 'page_title': 'Eventos | Registrar Evento', 'events_active': 'active',
               'address_form': address_form, 'event_form': event_form}
    return render(request, 'events/events_register/create_event.html', context)

@login_required
def delete_event(request, pk):
    event = Event.objects.get(id=pk)
    address = Address.objects.get(id=event.address.id)

    try:
        event.delete()
        address.delete()

        messages.success(request, 'O evento foi removido com sucesso!',
                         extra_tags='alert alert-success alert-dismissible fade show')
    except:
        messages.error(request, 'Falha na execução. Tente novamente.',
                       extra_tags='alert alert-danger alert-dismissible fade show')

    return redirect('events:home')


@login_required
def edit_event(request, pk):
    context = {}

    event = Event.objects.get(id=pk)
    address = Address.objects.get(id=event.address.id)

    if request.method == "POST":
        event_form = EventForm(request.POST)
        address_form = AddressForm(request.POST)

        if address_form.is_valid() and event_form.is_valid():
            instance = address_form.instance  # This is the new object being saved
            instance.id = address.id
            instance.created_at = address.created_at
            instance.save()

            instance = event_form.instance  # This is the new object being saved
            instance.id = event.id
            instance.address_id = address.id
            instance.created_at = event.created_at
            instance.save()

            messages.success(request, 'Evento atualizado com sucesso com sucesso!',
                             extra_tags='alert alert-success alert-dismissible fade show')

            return redirect('events:home')
        else:
            messages.error(request, 'Por favor corrija os erros abaixo para continuar.', extra_tags='alert alert-danger alert-dismissible fade show')
    else:
        address_form = AddressForm(instance=address)
        event_form = EventForm(instance=event)

        context['address_form'] = address_form
        context['event_form'] = event_form

    context['pagina'] = 'Eventos'
    context['page_title'] = 'Eventos | Editar infomações'
    context['events_active'] = 'active'

    return render(request, 'events/events_register/edit_event.html', context)