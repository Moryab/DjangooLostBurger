# Generated by Django 5.0.6 on 2024-07-08 09:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0018_perfil_prefijo_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallepedido',
            name='precio_unitario',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='subtotal',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='total',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
