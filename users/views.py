import secrets

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from config.settings import EMAIL_HOST_USER
from mailingservice.forms import MailingModeratorForm
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'mailingservice.can_view_user_list'


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User


class UserCreateView(CreateView):
    # создаем пользователя
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:user_login')

    def form_valid(self, form):
        # Валидируем пользователя автоматической отправкой сообщения на ящик
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}"
        send_mail(
            subject="Подтверждение электронного адреса",
            message=f"Приветствую!!! Прошу перейти по ссылке {url} для подтверждения почты",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    # Верифицируем пользователя по отправленному/полученному токену
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:user_login"))


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = User
    fields = ('id', 'user_email', 'is_active')
    success_url = reverse_lazy('users:user_list')

    def get_form_class(self):
        user = self.request.user
        if user.has_perm("mailingservice.can_view_user_list") and user.has_perm("mailingservice.can_block_user"):
            return MailingModeratorForm
        raise PermissionDenied


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('users:user_list')
