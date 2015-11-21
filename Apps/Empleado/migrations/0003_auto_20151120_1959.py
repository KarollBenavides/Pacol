# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleado', '0002_auto_20151120_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=50)),
                ('ciudad', models.ForeignKey(to='Empleado.Ciudad')),
            ],
        ),
        migrations.AddField(
            model_name='sucursal',
            name='ubicacion',
            field=models.ForeignKey(to='Empleado.Ubicacion'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(to='Empleado.Pais'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(to='Empleado.Departamento'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='sucursal',
            field=models.ForeignKey(to='Empleado.Sucursal'),
            preserve_default=False,
        ),
    ]
