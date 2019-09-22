from django.contrib.auth import login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, RedirectView, TemplateView
from django.contrib import messages
from core.forms import LoginForm, UpdatePasswordForm
from django.contrib.auth.forms import PasswordChangeForm


class HomeView(TemplateView):
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
        messages.add_message(self.request, messages.SUCCESS, 'User authenticated successfully')
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Failed to authenticate')
        return super(LoginView, self).form_invalid(form)


class LogoutView(RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(self.request, messages.SUCCESS, 'User successfully logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)


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
