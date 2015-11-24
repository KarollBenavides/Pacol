# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'verbose_name_plural': 'Proveedores'},
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nit',
            field=models.IntegerField(unique=True),
        ),
    ]
