from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone"}),
            "password1": forms.PasswordInput(attrs={"placeholder": "Enter password"}),
            "password2": forms.PasswordInput(attrs={"placeholder": "Confirm password"}),
        }
        fields = UserCreationForm.Meta.fields + ("phone", "is_admin")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
