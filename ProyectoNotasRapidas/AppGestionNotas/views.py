from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import UserRegisterForm, PostForm
from django.contrib import messages

# Create your views here.


def feed(request):
    notas = Nota.object.all()

    context = {'notas': notas}
    return render(request, 'AppGestionNotas/feed.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
        else:
            form = UserRegisterForm()

        context = {'form': form}
        return render(request, 'AppGestionNotas/register.html', context)


def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'AppGestionNotas/post.html', {'form': form})


def profile(request):
    return render(request, 'AppGestionNotas/profile.html')


def saludo(request):  # primera vista

    return HttpResponse("hola")
