# Generated by Django 4.2.2 on 2023-06-14 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_alter_cliente_puntos_alter_factura_montototal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factura',
            old_name='MontoTotal',
            new_name='montoTotal',
        ),
    ]
