# Generated by Django 5.0.4 on 2024-04-17 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_Rol', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('cedula', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_emp', models.CharField(max_length=20)),
                ('correo_emp', models.CharField(max_length=30)),
                ('contrasena_emp', models.CharField(max_length=128)),
                ('tel_emp', models.CharField(max_length=10)),
                ('direc_emp', models.CharField(max_length=30)),
                ('ciudad_emp', models.CharField(max_length=20)),
                ('foto_emp', models.ImageField(upload_to='empleado/')),
                ('ID_Rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerente.rol')),
            ],
        ),
    ]