# Generated by Django 4.1.3 on 2022-12-06 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestionNotas', '0007_rename_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='AppGestionNotas.user'),
        ),
    ]