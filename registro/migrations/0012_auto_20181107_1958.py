# Generated by Django 2.1.3 on 2018-11-07 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0011_auto_20181107_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rota',
            name='Motorista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.Motorista'),
        ),
    ]