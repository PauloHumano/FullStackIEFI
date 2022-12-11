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
from AppGestionUsuarios.models import *
from .serializers import *

"""
from django.http import HttpResponse, HttpResponseRedirect
from django.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.decorators import never_cache


from AppGestionNotas.serializers import *
"""

# Create your views here.


def gestionNota(request):
    notas = Nota.objects.all()
    context = {'notas': notas}
    return render(
        request,
        "AppGestionNotas/gestionNota.html",
        context)


def registrarNota(request):
    user = request.POST['txtuser']
    content = request.POST['txtcontent']

    Nota.objects.create(user_id=user, content=content)

    return redirect('gestionNota')


def edicionNota(request, timestamp):
    nota = Nota.objects.get(timestamp=timestamp)
    context = {"nota": nota}
    return render(request, "edicionNota.html", context)


def editarNota(request):
    username = request.POST['username']
    timestamp = request.POST['timestamp']
    content = request.POST['content']

    nota = Nota.objects.get(username, timestamp=timestamp, content=content)
    nota.timestamp = timestamp
    nota.content = content
    nota.save()

    return redirect('/')


def eliminarNota(request, timestamp):
    nota = Nota.objects.get(timestamp=timestamp)
    nota.delete()

    return redirect('/')


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
