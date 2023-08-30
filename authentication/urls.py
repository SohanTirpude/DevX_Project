from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.singup, name='singup'),
    path('singin/', views.singin, name='singin'),
    path('home/', views.home, name='home'),
    path('singout/', views.singout, name='singout'),
]