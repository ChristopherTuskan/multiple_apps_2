from django.urls import path
from . import views

urlpatterns = [
    path('users', views.index),
    path('users/new', views.register),
    path('users/login', views.login),
    path('users/register', views.register),
]