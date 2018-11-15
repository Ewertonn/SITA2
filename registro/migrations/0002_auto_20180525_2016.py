# Generated by Django 2.0.5 on 2018-05-25 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('Motorista_id', models.AutoField(primary_key=True, serialize=False)),
                ('Motorista_nome', models.CharField(max_length=100)),
                ('Motorista_idade', models.CharField(max_length=3)),
                ('Motorista_contato', models.CharField(max_length=15)),
                ('Motorista_sexo', models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('Rota_id', models.AutoField(primary_key=True, serialize=False)),
                ('Rota_pontopartida', models.CharField(max_length=100)),
                ('Rota_pontochegada', models.CharField(max_length=100)),
                ('Rota_horario', models.DateTimeField()),
                ('Rota_motorista', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='registro.Motorista')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('Veiculo_id', models.AutoField(primary_key=True, serialize=False)),
                ('Veiculo_modelo', models.CharField(max_length=50)),
                ('Veiculo_motorista', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='registro.Motorista')),
                ('Veiculo_rota', models.ManyToManyField(to='registro.Rota')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='Usuario_contato',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Usuario_idade',
            field=models.CharField(max_length=3),
        ),
        migrations.AddField(
            model_name='rota',
            name='Rota_veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='registro.Veiculo'),
        ),
        migrations.AddField(
            model_name='motorista',
            name='Motorista_veiculo',
            field=models.ManyToManyField(to='registro.Veiculo'),
        ),
    ]
