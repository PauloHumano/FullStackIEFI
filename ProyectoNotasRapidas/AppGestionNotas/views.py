# Django
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import UserRegisterForm, PostForm
from .models import *
from .serializers import *

"""
from django.http import HttpResponse, HttpResponseRedirect
from django.decorators.csrf import csrf_protect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators import never_cache


from AppGestionNotas.serializers import *
"""

# Create your views here.


def gestionrapida(request):
    notas = Nota.objects.all()
    context = {'notas': notas}
    return render(request, "AppGestionNotas/gestionrapida.html", context)


def feed(request):
    notas = Nota.objects.all()

    context = {'notas': notas}
    return render(request, 'AppGestionNotas/feed.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'appgestionnotas/register.html', context)


def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'post enviado')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'appgestionnotas/register.html', {'form': form})


def profile(request):
    return render(request, 'AppGestionNotas/profile.html')


def show_index(request):
    return render(request, 'base/index.html')

# login, logout, loginRequiredMixin


class Login(LoginView):
    next_page = reverse_lazy('main')
    template_name = 'login.html'


class Logout(LogoutView):
    next_page = reverse_lazy('login')


class Main(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'main.html'


class UserAPIVIEW(APIView):

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
