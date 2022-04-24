from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import RegisterForm, AuthorizationForm
from .models import Recipe
from .utils import is_liked
from bot_directory.start_bot import send_message_to_admin


def index(request):
    data = {'title': 'Recipe Book'}
    return render(request, "first_lab/index.html", context=data)


def about_us(request):
    data = {'title': 'About Us'}
    return render(request, "first_lab/about_us.html", context=data)


class RecipesListView(ListView):
    model = Recipe
    template_name = 'first_lab/recipes.html'
    context_object_name = "recipes"
    # allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs["title"] = "Recipes"
        context = super().get_context_data(**kwargs)
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'first_lab/recipe_detail.html'
    context_object_name = "recipe"
    # allow_empty = False

    def get_context_data(self, *args, object_list=None, **kwargs):
        flag = is_liked(self.request.user, kwargs.get("object"))
        # print(flag)
        kwargs["flag"] = flag
        context = super().get_context_data(**kwargs)
        return context


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'first_lab/register.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs["title"] = "Registration"
        context = super().get_context_data(**kwargs)
        return context

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

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs["title"] = "Authorization"
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy("index")


def logout_user(request):
    logout(request)
    return redirect('index')


# def test(request):
#     return render(request, "first_lab/recipe_detail.html")
