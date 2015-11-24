from django.db import models

# Create your models here.
from Apps.Empleado.models import Empleado, Ubicacion, Pais, Departamento, Ciudad


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    nit = models.IntegerField(unique=True)
    telefono = models.IntegerField()
    ubicacion = models.OneToOneField(Ubicacion)

    class Meta:
        verbose_name_plural = "Proveedores"

    def __unicode__(self):
        return "{0}".format(self.nombre)


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return "{0}".format(self.nombre)


class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor)
    categoria = models.ForeignKey(Categoria)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=80)

    def __unicode__(self):
        return "{0}".format(self.nombre)


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    cedula = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)

    def __unicode__(self):
        return "{0}".format(self.nombre)


class Factura(models.Model):
    total = models.IntegerField()
    cliente = models.ForeignKey(Cliente)
    empleado = models.ForeignKey(Empleado)
    producto = models.ForeignKey(Producto)

    def __unicode__(self):
        return "Factura No {0} a nombre de {1}".format(self.id, self.cliente.nombre)




class Venta(models.Model):
    empleado = models.ForeignKey(Empleado)
    factura = models.ForeignKey(Factura)

    def __unicode__(self):
        return "Venta realizada por {0}".format(self.empleado)




