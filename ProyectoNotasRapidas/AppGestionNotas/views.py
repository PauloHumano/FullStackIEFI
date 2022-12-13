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


def edicionNota(request, id):
    nota = Nota.objects.get(id=id)
    return render(request, "AppGestionNotas/edicionNota.html", {"nota": nota})


def eliminarNota(request, id):
    nota = Nota.objects.get(id=id)
    nota.delete()

    return redirect('gestionNota')


def editarNota(request):
    id = request.POST['txtuser']
    content = request.POST['txtcontent']

    nota = Nota.objects.get(id=id)
    nota.id = id
    nota.content = content
    nota.save()

    return redirect('gestionNota')


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
