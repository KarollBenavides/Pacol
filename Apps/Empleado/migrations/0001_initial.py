# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('sueldo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('cedula', models.IntegerField()),
                ('cargo', models.ForeignKey(to='Empleado.Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Sucursales',
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=50)),
                ('ciudad', models.ForeignKey(to='Empleado.Ciudad')),
            ],
            options={
                'verbose_name_plural': 'Ubicaciones',
            },
        ),
        migrations.AddField(
            model_name='sucursal',
            name='ubicacion',
            field=models.ForeignKey(to='Empleado.Ubicacion'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='sucursal',
            field=models.ForeignKey(to='Empleado.Sucursal'),
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
    ]
