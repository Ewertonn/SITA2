# Generated by Django 2.1.3 on 2018-11-14 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registro', '0014_auto_20181113_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='Reserva_usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Usuario_reserva',
        ),
        migrations.AddField(
            model_name='reserva',
            name='Usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
