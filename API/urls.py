from django.urls import path
from . import views

urlpatterns = [
    path('set_like/', views.LikesView.as_view(), name="set_like"),
]
