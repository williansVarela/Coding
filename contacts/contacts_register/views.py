# -*- encoding:utf-8 -*-
from django.contrib.auth.decorators import login_required
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
