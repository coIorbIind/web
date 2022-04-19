from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from first_lab.forms import RegisterForm, AuthorizationForm
from bot_directory.start_bot import send_message_to_admin


def index(request):
    data = {'title': 'Recipe Book'}
    return render(request, "first_lab/index.html", context=data)


def about_us(request):
    data = {'title': 'About Us'}
    return render(request, "first_lab/about_us.html", context=data)


def register(request):
    data = {'title': 'Register'}
    return render(request, "first_lab/register.html", context=data)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'first_lab/register.html'
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = None
        form = self.get_form()
        if form.is_valid():
            username = form.cleaned_data.get("username")
            user_email = form.cleaned_data.get("email")
            send_message_to_admin(f"Зарегистрирован новый пользователь!\n"
                                  f"Username: {username}\n"
                                  f"Электронная почта: {user_email}")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class AuthorizationView(LoginView):
    form_class = AuthorizationForm
    template_name = 'first_lab/authorization.html'
    # success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse_lazy("index")


def test(request):
    return render(request, "first_lab/recipe_book.html")


def logout_user(request):
    logout(request)
    return redirect('index')
