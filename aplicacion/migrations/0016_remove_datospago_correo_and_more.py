# Generated by Django 5.0.6 on 2024-07-03 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0015_remove_datospago_direccion_facturacion_igual_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datospago',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='datospago',
            name='nombre_completo',
        ),
    ]
