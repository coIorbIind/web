from django.contrib import admin
from first_lab.models import Profile, Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "likes_count")
    search_fields = ("title", )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # list_display = ("id", "user__email")
    pass
