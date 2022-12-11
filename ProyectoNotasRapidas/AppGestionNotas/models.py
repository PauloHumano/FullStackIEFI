from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
# ClassPost --- ClassNota



class Nota(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='usernotas')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'
