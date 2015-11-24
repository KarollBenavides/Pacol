# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('cedula', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.IntegerField()),
                ('cliente', models.ForeignKey(to='Ventas.Cliente')),
                ('empleado', models.ForeignKey(to='Empleado.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=80)),
                ('categoria', models.ForeignKey(to='Ventas.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('nit', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('ubicacion', models.OneToOneField(to='Empleado.Ubicacion')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('empleado', models.ForeignKey(to='Empleado.Empleado')),
                ('factura', models.ForeignKey(to='Ventas.Factura')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(to='Ventas.Proveedor'),
        ),
        migrations.AddField(
            model_name='factura',
            name='producto',
            field=models.ForeignKey(to='Ventas.Producto'),
        ),
    ]
