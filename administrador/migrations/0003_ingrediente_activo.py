# Generated by Django 5.0.4 on 2024-05-01 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_ensaladas_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingrediente',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
