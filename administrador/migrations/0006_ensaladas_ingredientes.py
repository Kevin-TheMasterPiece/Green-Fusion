# Generated by Django 5.0.4 on 2024-05-05 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0005_ensaladas_categoria_alter_recetas_fk_id_ensalada_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ensaladas',
            name='ingredientes',
            field=models.ManyToManyField(through='administrador.recetas', to='administrador.ingrediente'),
        ),
    ]
