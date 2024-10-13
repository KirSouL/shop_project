from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, UserChangeForm
from django import forms

from users.models import User


class StyleFormMixin:
    """Класс примесь для стилизации форм пользователей"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegistrateForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserPasswordResetForm(StyleFormMixin, PasswordResetForm):
    class Meta:
        model = User
        fields = ('email',)


class UserProfileForm(StyleFormMixin, UserChangeForm):
    """Форма для изменения информации о пользователе"""
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone", "avatar",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = forms.HiddenInput()
