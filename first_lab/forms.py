from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Recipe


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
                {"placeholder": "Repeat Password", "class": "input-field", "id": "repeat-password",
                 "type": "password"})))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AuthorizationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs=({"placeholder": "Name", "class": "input-field", "id": "username"})))
    password = forms.CharField(
        widget=forms.TextInput(
            attrs=({"placeholder": "Password", "class": "input-field", "id": "password", "type": "password"})))


class RecipeCreationForm(ModelForm):

    class Meta:
        model = Recipe
        fields = ("title", "photo", "ingredients", "directions")
        widgets = {
            'title': forms.TextInput(attrs={"class": "form_settings", "type": "text", "size": "30", "maxlength": "50"}),
            "photo": forms.FileInput(
                attrs={"class": "form_settings", "type": "file", "name": "photo", "accept": "image/*,image  /jpeg"}),
        }
