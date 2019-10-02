# -*- encoding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from contacts.contacts_register.forms import ContactForm, AddressForm, PersonForm
from contacts.contacts_register.models import Contact, Person, Address
from django.contrib import messages
from django.shortcuts import render, redirect


@login_required
def register_contact(request):
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        person_form = PersonForm(request.POST)
        contact_form = ContactForm(request.POST)
        if address_form.is_valid() and person_form.is_valid() and contact_form.is_valid():
            address = address_form.save()
            person = person_form.save(commit=False)
            contact = contact_form.save(commit=False)
            person.address = address
            person.save()
            contact.person = person
            contact.save()

            messages.success(request, 'Contato adicionado com sucesso!', extra_tags='alert alert-success alert-dismissible fade show')

            return redirect('contacts:create_contact')
        else:
            messages.error(request, 'Por favor corrija o erro acima para continuar.', extra_tags='alert alert-danger alert-dismissible fade show')
    else:
        address_form = AddressForm()
        person_form = PersonForm()
        contact_form = ContactForm()

    context = {'pagina': 'Admin', 'page_title': 'Admin | Registrar Usuário', 'contacts_active': 'active',
               'address_form': address_form, 'person_form': person_form, 'contact_form': contact_form}
    return render(request, 'contacts/contacts_register/create_contact.html', context)


@login_required
def delete_contact(request, pk):
    contact = Contact.objects.get(id=pk)
    person = Person.objects.get(id=contact.person.id)
    address = Address.objects.get(id=person.address.id)

    try:
        contact.delete()
        person.delete()
        address.delete()
        messages.success(request, 'O Contato de {} foi removido com sucesso!'.format(person.name),
                         extra_tags='alert alert-success alert-dismissible fade show')
    except:
        messages.error(request, 'Falha na execução. Tente novamente.',
                       extra_tags='alert alert-danger alert-dismissible fade show')

    return redirect('contacts:home')

@login_required
def edit_contact(request, pk):
    context = {}

    contact = Contact.objects.get(id=pk)
    person = Person.objects.get(id=contact.person.id)
    address = Address.objects.get(id=person.address.id)

    if request.method == "POST":
        address_form = AddressForm(request.POST)
        person_form = PersonForm(request.POST)
        contact_form = ContactForm(request.POST)

        if address_form.is_valid() and person_form.is_valid() and contact_form.is_valid():
            instance = address_form.instance  # This is the new object being saved
            instance.id = address.id
            instance.created_at = address.created_at
            instance.save()

            instance = person_form.instance  # This is the new object being saved
            instance.id = person.id
            instance.address_id = address.id
            instance.created_at = person.created_at
            instance.save()

            instance = contact_form.instance  # This is the new object being saved
            instance.id = contact.id
            instance.person_id = person.id
            instance.created_at = contact.created_at
            instance.save()

            messages.success(request, 'Contato de {} atualizado com sucesso com sucesso!'.format(person.name),
                             extra_tags='alert alert-success alert-dismissible fade show')

            return redirect('contacts:home')
        else:
            messages.error(request, 'Por favor corrija os erros abaixo para continuar.', extra_tags='alert alert-danger alert-dismissible fade show')
    else:


        address_form = AddressForm(instance=address)
        person_form = PersonForm(instance=person)
        contact_form = ContactForm(instance=contact)

        context['address_form'] = address_form
        context['person_form'] = person_form
        context['contact_form'] = contact_form

    context['pagina'] = 'Contatos'
    context['page_title'] = 'Contatos | Editar infomações'
    context['contacts_active'] = 'active'

    return render(request, 'contacts/contacts_register/edit_contact.html', context)


class UpdateContact(LoginRequiredMixin, UpdateView):
    template_name = 'contacts/contacts_register/edit_contact.html'
    pk_url_kwarg = 'templates_pk'
    form_classes = {'contact': ContactForm,
                    'person': PersonForm,
                    'address': AddressForm}
    success_url = reverse_lazy('contacts:edit_contact')

    def get_context_data(self, **kwargs):
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        context['pagina'] = 'Contatos'
        context['page_title'] = 'Contatos | Editar Informações'
        context['contacts_active']: 'active'

        return context

    def get_object(self, queryset=None):
        """This loads the profile of the currently logged in user"""

        contact = Contact.objects.get(id=pk)
        person = Person.objects.get(id=contact.person.id)
        address = Address.objects.get(id=person.address.id)

        objects = {'contact': contact,
                   'person': person,
                   'address': address}

        return objects

    def form_valid(self, form):
        """Here is where you set the user for the new profile"""

        instance = form.instance  # This is the new object being saved
        instance.user = self.request.user
        instance.save()

        if form.is_valid():
            messages.success(self.request, 'Seus dados foram atualizado com sucesso!', extra_tags='alert alert-success')
        else:
            messages.error(self.request, 'Por favor corrija o erro acima.', extra_tags='alert alert-danger')

        return super(UpdateProfile, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        address_form = AddressForm(request.POST)
        person_form = PersonForm(request.POST)
        contact_form = ContactForm(request.POST)
        if address_form.is_valid() and person_form.is_valid() and contact_form.is_valid():
            address = address_form.save()
            person = person_form.save(commit=False)
            contact = contact_form.save(commit=False)
            person.address = address
            person.save()
            contact.person = person
            contact.save()

            messages.success(request, 'Contato adicionado com sucesso!',
                             extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('contacts:create_contact')
        else:
            messages.error(request, 'Por favor corrija o erro acima para continuar.',
                           extra_tags='alert alert-danger alert-dismissible fade show')

        return redirect(reverse_lazy("contacts:home"))