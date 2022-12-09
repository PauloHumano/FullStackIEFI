# Django
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
# appGestionNotas
# from .models import *
# fPerfil----fUser
# Imagenes---Nota


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='confirma contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'rows': 2, 'placeholder': 'que pasa?'}), required=True)

    class Meta:
        model = Perfil
        fields = ['content']
