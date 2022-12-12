from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Perfil


@receiver(post_save, sender=User)
def created_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
