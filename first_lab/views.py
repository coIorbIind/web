from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import RegisterForm, AuthorizationForm, RecipeCreationForm
from .models import Recipe
from .utils import is_liked
from bot_directory.start_bot import send_message_to_admin


def index(request):
    lang = request.COOKIES.get("language", "EN")
    data = {'title': 'Книга рецептов' if lang == "RU" else 'Recipe Book', 'lang': lang}
    return render(request, "first_lab/index.html", context=data)


def about_us(request):
    lang = request.COOKIES.get("language", "EN")
    data = {'title': 'О нас' if lang == "RU" else 'About Us', 'lang': lang}
    return render(request, "first_lab/about_us.html", context=data)


class RecipesListView(ListView):
    model = Recipe
    template_name = 'first_lab/all_recipes.html'
    context_object_name = "recipes"
    # allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs["lang"] = self.request.COOKIES.get("language", "EN")
        kwargs["title"] = "Рецепты" if kwargs["lang"] == "RU" else "Recipes"
        context = super().get_context_data(**kwargs)
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'first_lab/recipe_detail.html'
    context_object_name = "recipe"

    def get_context_data(self, *args, **kwargs):
        flag = is_liked(self.request.user, kwargs.get("object"))
        # print(flag)
        kwargs["flag"] = flag
        kwargs["lang"] = self.request.COOKIES.get("language", "EN")
        kwargs["title"] = self.object.title
        context = super().get_context_data(**kwargs)
        return context


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'first_lab/register.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs["lang"] = self.request.COOKIES.get("language", "EN")
        kwargs["title"] = "Регистрация" if kwargs["lang"] == "RU" else "Registration"
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
        kwargs["lang"] = self.request.COOKIES.get("language", "EN")
        kwargs["title"] = "Авторизация" if kwargs["lang"] == "RU" else "Authorization"
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy("index")


def logout_user(request):
    logout(request)
    return redirect('index')


class CreateRecipeView(CreateView):
    form_class = RecipeCreationForm
    template_name = 'first_lab/create_recipe.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs["lang"] = self.request.COOKIES.get("language", "EN")
        kwargs["title"] = "Создание рецепта" if kwargs["lang"] == "RU" else "Create Recipe"
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = None
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user.profile
            new_post.save()

            self.object = form.save()

            return HttpResponseRedirect(reverse_lazy('recipe', args=(self.object.id, )))

        return self.form_invalid(form)
