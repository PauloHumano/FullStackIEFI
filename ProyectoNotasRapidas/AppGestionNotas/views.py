from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def feed(request):
    posts = Post.object.all()

    context = {'posts': posts}
    return render(request, 'social/feed.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            message.sucess(request, f'Usuario {username} creado')
        else:
            form = UserCreationForm()

        context = {'form': form}
        return render(request, 'social/register.html', context)


def profile(request):
    return render(request, 'social/profile.html')


def saludo(request):  # primera vista

    return HttpResponse("hola")
