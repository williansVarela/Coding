# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, RedirectView, TemplateView, View
from django.contrib import messages
from core.forms import LoginForm, UpdatePasswordForm, EditProfileForm, UserCreateForm
from django.views.generic import UpdateView
from core.models import User
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from donation.models import Donation
from finance.models import Expense
from animal.models import Shelter, Animal
from django.db.models import Sum, Count


def admin_check(user):
    return user.is_admin


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.add_message(self.request, messages.SUCCESS, 'Usuário autenticado com sucesso!')
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Falha ao autenticar usuário.')
        return super(LoginView, self).form_invalid(form)


class LogoutView(RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(self.request, messages.SUCCESS, 'Usuário desconectado com sucesso!')
        return super(LogoutView, self).get(request, *args, **kwargs)


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = 'login/'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['pagina'] = 'Dashboard'
        context['page_title'] = 'Home | Dashboard'
        context['home_active'] = 'active'
        context['donations'] = Donation.objects.all()
        context['animals'] = Animal.objects.all()
        context['total_donations'] = Donation.objects.aggregate(Sum('amount'))
        context['finances'] = Expense.objects.all()
        context['total_finance'] = Expense.objects.aggregate(Sum('amount'))
        queryset = Shelter.objects.filter(category__icontains='adoção')
        context['total_adoption'] = queryset.aggregate(Count('animal'))
        queryset = Shelter.objects.filter(category__icontains='temp')
        context['total_animals'] = queryset.aggregate(Count('animal'))




        return context


@login_required
@user_passes_test(admin_check)
def register_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso!', extra_tags='alert alert-success')
            return redirect('create_user')
        else:
            messages.error(request, 'Por favor corrija o erro acima para continuar.', extra_tags='alert alert-danger')
    else:
        form = UserCreateForm()

    context = {'pagina': 'Admin', 'page_title': 'Admin | Registrar Usuário', 'admin_active': 'active', 'form': form}
    return render(request, 'create_user.html', context)


@login_required
@user_passes_test(admin_check)
def list_users(request):
    users = get_user_model()
    context = {'pagina': 'Lista de Usuários', 'page_title': 'Admin | Usuários', 'admin_active': 'active'}
    context['users'] = users.objects.all()
    context['template_modal'] = 'modal_confirm.html'
    context['object_model'] = 'usuário'
    context['title_model'] = 'Remover Usuário'
    context['url_modal'] = 'delete_user'



    return render(request, 'user_list.html', context)


@login_required
@user_passes_test(admin_check)
def disable_user(request, pk):
    user = User.objects.get(id=pk)
    if user.is_active:
        user.is_active = False
        user.save()
        messages.success(request, 'Usuário {} desativado com sucesso!'.format(user.email),
                         extra_tags='alert alert-success alert-dismissible fade show')
    else:
        messages.error(request, 'Conta de usuário já está ativa!',
                       extra_tags='alert alert-danger alert-dismissible fade show')

    return redirect('list_users')


@login_required
@user_passes_test(admin_check)
def active_user(request, pk):
    user = User.objects.get(id=pk)
    if not user.is_active:
        user.is_active = True
        user.save()
        messages.success(request, 'Usuário {} ativado com sucesso!'.format(user.email),
                         extra_tags='alert alert-success alert-dismissible fade show')
    else:
        messages.error(request, 'Conta de usuário já está desativada!',
                       extra_tags='alert alert-danger alert-dismissible fade show')

    return redirect('list_users')


@login_required
@user_passes_test(admin_check)
def delete_user(request, pk):
    user = User.objects.get(id=pk)
    try:
        user.delete()
        messages.success(request, 'Usuário {} removido com sucesso!'.format(user.email), extra_tags='alert alert-success alert-dismissible fade show')
    except:
        messages.error(request, 'Falha na execução. Tente novamente.', extra_tags='alert alert-danger alert-dismissible fade show')

    return redirect('list_users')


@login_required
def change_password(request):
    context = {'pagina': 'Perfil', 'page_title': 'Perfil | Alterar Senha'}

    if request.method == 'POST':
        form = UpdatePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Sua senha foi atualizada com sucesso!', extra_tags='alert alert-success')
            return redirect('change_password')
        else:
            messages.error(request, 'Por favor corrija o erro acima.', extra_tags='alert alert-danger')
    else:
        form = UpdatePasswordForm(request.user)

    context['form'] = form

    return render(request, 'change_password.html', context)


class UpdateProfile(LoginRequiredMixin, UpdateView):
    template_name = 'update_profile.html'
    form_class = EditProfileForm
    model = User
    success_url = reverse_lazy('update_profile')

    def get_context_data(self, **kwargs):
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        context['pagina'] = 'Perfil'
        context['page_title'] = 'Perfil | Editar Informações'

        return context

    def get_object(self, queryset=None):
        """This loads the profile of the currently logged in user"""

        return User.objects.get(email=self.request.user)

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


class EditProfile(LoginRequiredMixin, UpdateView):
    template_name = 'update_profile.html'
    form_class = EditProfileForm
    model = User
    success_url = reverse_lazy('list_users')

    def get_context_data(self, **kwargs):
        context = super(EditProfile, self).get_context_data(**kwargs)
        context['pagina'] = 'Perfil de usuário'
        context['page_title'] = 'Admin | Editar Usuário'

        return context

    def get_object(self, queryset=None):
        """This loads the profile of the user"""

        return User.objects.get(id=self.kwargs['pk'])

    def form_valid(self, form):
        """Here is where you set the user for the new profile"""

        instance = form.instance  # This is the new object being saved
        instance.user = self.request.user
        instance.save()

        if form.is_valid():
            messages.success(self.request, 'Os dados do usuário foram atualizado com sucesso!', extra_tags='alert alert-success')
        else:
            messages.error(self.request, 'Por favor corrija o erro acima.', extra_tags='alert alert-danger')

        return super(EditProfile, self).form_valid(form)

