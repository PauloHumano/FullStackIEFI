from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # no imagen

    def __str__(self):
        return f'Perfil de {self.user.username}'
