from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from first_lab.models import Profile, Recipe


class LikesView(APIView):

    def post(self, *args, **kwargs):
        # print(self.request.data)
        try:
            user = self.request.user
            profile = user.profile
            recipe_id = self.request.data.get("recipe_id")
            if recipe_id is None:
                raise AttributeError
            recipe = Recipe.objects.get(pk=recipe_id)

            # print(user)

            # print(profile.liked_publications.all())
            profile.liked_publications.add(recipe)
            profile.save()
            # print(profile.liked_publications.all())

            return Response(status=status.HTTP_200_OK)

        except AttributeError:
            content = {"error": "You have no profile"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        except User.profile.RelatedObjectDoesNotExist:
            content = {"error": "You have no profile"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        except Recipe.DoesNotExist:
            content = {"error": "There's no such recipe"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def delete(self, *args, **kwargs):
        # print(self.request.data)

        try:
            user = self.request.user
            profile = user.profile
            recipe_id = self.request.data.get("recipe_id")
            if recipe_id is None:
                raise AttributeError
            recipe = Recipe.objects.get(pk=recipe_id)

            # print(profile.liked_publications.all())
            profile.liked_publications.remove(recipe)
            # print(profile.liked_publications.all())
            profile.save()
            # print(profile.liked_publications.all())
            return Response(status=status.HTTP_200_OK)

        except AttributeError:
            content = {"error": "You have no profile"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        except User.profile.RelatedObjectDoesNotExist:
            content = {"error": "You have no profile"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        except Recipe.DoesNotExist:
            content = {"error": "There's no such recipe"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def get(self, *args, **kwargs):
        # print(self.request.query_params.get("pk"))
        try:
            recipe_id = self.request.query_params.get("pk")
            if recipe_id is None:
                raise AttributeError
            recipe = Recipe.objects.get(pk=recipe_id)
            data = {"likes_count": recipe.likes_count()}
            return Response(data, status=status.HTTP_200_OK)

        except AttributeError:
            content = {"error": "Yoops something wrong"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        except Recipe.DoesNotExist:
            content = {"error": "There's no such recipe"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
