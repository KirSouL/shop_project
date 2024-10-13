import secrets
import string
import random

from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegistrateForm, UserPasswordResetForm, UserProfileForm
from users.models import User


class UserRegistrateView(CreateView):
    model = User
    form_class = UserRegistrateForm
    template_name = "users/users_form.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(20)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}"
        send_mail(
            subject="Подтверждение почты пользователя",
            message=f"Данное сообщение получено автоматически\n"
                    f"Если это были не Вы выполните следующие действия:\n"
                    f"1. Смените пароль.\n"
                    f"2. Проверьте актуальность номера телефона.\n"
                    f"3. Обратитесь в поддержку\n"                    
                    f"Перейдите по ссылке для подверждения почты: {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email,]
        )
        return super().form_valid(form)


class UserPasswordResetView(PasswordResetView):
    model = User
    form_class = UserPasswordResetForm
    template_name = "users/password_reset.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        """Проверка существования пользователя и отправка нового пароля на почту"""
        email = form.cleaned_data["email"]
        user = User.objects.get(email=email)
        if user:
            new_password = ''
            for item in range(10):
                new_password += ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation)])
            user.set_password(new_password)
            user.is_active = True
            user.save()
            send_mail(
                subject="Восстановление пароля",
                message=f"Данное сообщение получено автоматически.\n"
                        f"По Вашему обращению был сгенерирован новый пароль.\n"
                        f"Ваш пароль: {new_password}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email, ]
            )
            return redirect(reverse("users:login"))


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user
