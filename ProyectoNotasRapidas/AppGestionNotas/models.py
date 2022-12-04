from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username


class NotasRapidas(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notasrapidas')
    content = models.TextField()

    def __str__(self):
        return f'{self.user.username}: {self.content}'
