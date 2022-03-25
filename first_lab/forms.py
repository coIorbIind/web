from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs=({"placeholder": "Name", "class": "input-field", "id": "username"})))
    email = forms.EmailField(
        widget=forms.TextInput(attrs=({"class": "input-field", "placeholder": "E-mail", "id": "e-mail"})))
    password1 = forms.CharField(
        widget=forms.TextInput(
            attrs=({"placeholder": "Password", "class": "input-field", "id": "password", "type": "password"})))
    password2 = forms.CharField(
        widget=forms.TextInput(
            attrs=(
            {"placeholder": "Repeat Password", "class": "input-field", "id": "repeat-password", "type": "password"})))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
