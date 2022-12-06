from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Perfil de {self.user.username}'


class Nota(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notas')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'
