# Generated by Django 5.0.6 on 2024-07-03 21:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0014_datospago_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datospago',
            name='direccion_facturacion_igual',
        ),
        migrations.AlterField(
            model_name='datospago',
            name='pedido',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='datos_pago', to='aplicacion.pedido'),
        ),
    ]
