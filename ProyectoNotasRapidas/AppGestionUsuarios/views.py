# Django
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import UserRegisterForm, PostForm
from .models import *
from .serializers import *

# Create your views here.


def home(request):
    return render(request, 'base/index.html')


class Main(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'main.html'


class gestionCrearNota(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('main')
    template_name = 'getionCrearNota.html'

# login, logout, loginRequiredMixin


class Login(LoginView):
    next_page = reverse_lazy('main')
    template_name = 'login.html'


class Logout(LogoutView):
    next_page = reverse_lazy('index')


class RegistroUsuario(CreateView):
    model = User
    template_name = 'AppGestionUsuarios/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'AppGestionUsuarios/register.html', context)


def profile(request):
    return render(request, 'AppGestionNotas/profile.html')


class UserAPIVIEW(APIView):

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
