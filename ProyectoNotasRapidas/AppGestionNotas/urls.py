"""ProyectoNotasRapidas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from AppGestionNotas.views import *
from . import views

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('registrarNota/', views.registrarNota, name='registrarNota'),
    path('editarNota/', views.editarNota, name='registrarNota'),
    path('edicionNota/<content>', views.edicionNota, name='edicionNota'),
    path('eliminarNota/<content>', views.eliminarNota, name='eliminarNota'),
    path('usuario/', UserAPIVIEW.as_view(), name='usuario_api'),
    path('list/', UserList.as_view(), name='usuario_list'),
]
