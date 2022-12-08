# Django
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import *
from .models import *
from .serializers import *

"""
from django.contrib import messages
from django.decorators.csrf import csrf_protect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators import never_cache


from AppGestionNotas.serializers import *
"""

# Create your views here.


def show_index(request):
    render(request, 'index.html')

# login, logout, loginRequiredMixin


class Login(LoginView):
    next_page = reverse_lazy('main')
    template_name = 'login.html'


class Logout(LogoutView):
    next_page = reverse_lazy('login')


class Main(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'main.html'


def vUser(request):
    if request.method == 'POST':
        form = fUser(data=request.POST)
        if form.is_valid():
            form.save()
            print('el formulario ha sido guardado')
        else:
            print('el formulario no es valido')
    else:
        form = fUser2()
    return render(request, 'perfil.html')


class UserAPIVIEW(APIView):

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
