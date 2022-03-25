from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test),
    # path('', views.index),
    # path('test_form/', views.test_form),
    path('', views.index, name='index'),
    path('about-us/', views.about_us, name='about-us'),
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('register/', views.register, name='register')
    # path('menu/', views.menu, name='main_menu'),
    # path('category/<cat_name>', views.cat_detail, name='cats')
]
