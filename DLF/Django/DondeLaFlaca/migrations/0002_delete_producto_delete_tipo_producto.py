# Generated by Django 5.0.6 on 2024-07-04 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DondeLaFlaca', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='Tipo_producto',
        ),
    ]
