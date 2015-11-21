# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='cedula',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='telefono',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]
