# Generated by Django 4.1.3 on 2022-12-04 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestionNotas', '0003_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
