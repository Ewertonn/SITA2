# Generated by Django 2.0.4 on 2018-08-17 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0007_auto_20180817_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorista',
            name='Motorista_contato',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='Usuario_contato',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
