# Generated by Django 5.0.4 on 2024-04-17 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerente', '0006_empleado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='ID_Rol',
            new_name='FK_ID_Rol',
        ),
    ]
