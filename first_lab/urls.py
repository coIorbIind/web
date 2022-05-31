from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about_us, name='about-us'),
    path("recipes/", views.RecipesListView.as_view(), name="recipes"),
    path("recipe/<int:pk>", views.RecipeDetailView.as_view(), name="recipe"),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('create_recipe/', views.CreateRecipeView.as_view(), name='create_recipe'),
    path('authorization/', views.AuthorizationView.as_view(), name='authorization'),
    path('logout/', views.logout_user, name='logout'),
]
