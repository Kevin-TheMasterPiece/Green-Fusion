# Generated by Django 5.0.4 on 2024-05-15 03:36

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0008_ingrediente_categoria'),
        ('store', '0008_delete_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factura',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='factura',
            name='total',
        ),
        migrations.AddField(
            model_name='factura',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='factura',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='factura',
            name='direccion',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='factura',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='factura',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='factura_ensalda',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='factura_ensalda',
            name='FK_ensalada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='administrador.ensaladas'),
        ),
        migrations.AlterField(
            model_name='factura_ensalda',
            name='FK_factura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.factura'),
        ),
        migrations.AddIndex(
            model_name='factura',
            index=models.Index(fields=['-created'], name='store_factu_created_149f93_idx'),
        ),
    ]
