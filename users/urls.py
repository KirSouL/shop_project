from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from users.forms import StyleFormMixin
from users.views import UserRegistrateView, email_verification, UserPasswordResetView, UserProfileView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registrate/', UserRegistrateView.as_view(), name='registrate'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
