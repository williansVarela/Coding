from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, RedirectView, TemplateView
from django.contrib import messages
from core.forms import LoginForm, UpdatePasswordForm, EditProfileForm, UserCreateForm


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = 'login/'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['pagina'] = 'Início'
        context['page_title'] = 'Home | Sistema de Gestão'
        context['home_active'] = 'active'

        return context


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


def admin_check(user):
    return user.is_admin


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
            messages.error(request, 'Por favor corrija o erro acima.', extra_tags='alert alert-danger')
    else:
        form = UserCreateForm()

    context = {'pagina': 'Admin', 'page_title': 'Admin | Registrar Usuário', 'admin_active': 'active', 'form': form}

    return render(request, 'create_user.html', context)


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


@login_required
def update_profile(request):
    context = {'pagina': 'Perfil', 'page_title': 'Perfil | Editar Informações'}

    if request.method == 'POST':
        form = EditProfileForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Seus dados foram atualizado com sucesso!', extra_tags='alert alert-success')
            return redirect('update_profile')
        else:
            messages.error(request, 'Por favor corrija o erro acima.', extra_tags='alert alert-danger')
    else:
        form = EditProfileForm(request.user)

    context['form'] = form

    return render(request, 'update_profile.html', context)
