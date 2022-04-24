from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    liked_publications = models.ManyToManyField("Recipe", related_name="users_who_liked",
                                                verbose_name="Понравившиеся рецепты")

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Recipe(models.Model):
    title = models.CharField(verbose_name="Название", max_length=50)
    photo = models.ImageField(verbose_name="Фото")
    ingredients = models.TextField(verbose_name="Ингридиенты")
    directions = models.TextField(verbose_name="Шаги")
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, verbose_name="Author", on_delete=models.CASCADE)

    def likes_count(self):
        return self.users_who_liked.count()

    def __str__(self):
        return f"\"{self.title}\" by {self.author}"

    def get_absolute_url(self):
        return reverse("recipe", kwargs={"pk": self.pk})
