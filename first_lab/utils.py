from .models import Recipe
from django.contrib.auth.models import User


def is_liked(user: User, recipe: Recipe) -> bool:
    try:
        return recipe in user.profile.liked_publications.all()

    except AttributeError:
        return False

