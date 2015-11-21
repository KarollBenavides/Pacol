from django.db import models

# Create your models here.

class Pais(models.Model):

    nombre = models.CharField(max_length = 50)

    class Meta:
        verbose_name_plural = "Paises"

    def __unicode__(self):
        return "{0}".format(self.nombre)


class Departamento(models.Model):

    nombre = models.CharField(max_length = 50)
    pais = models.ForeignKey(Pais)

    class Meta:
        verbose_name_plural = "Departamentos"

    def __unicode__(self):
        return "{0}".format(self.nombre)


class Ciudad(models.Model):

    nombre = models.CharField(max_length = 50)
    departamento = models.ForeignKey(Departamento)

    class Meta:
        verbose_name_plural = "Ciudades"


class Ubicacion(models.Model):

    direccion = models.CharField(max_length = 50)
    ciudad = models.ForeignKey(Ciudad)

    class Meta:
        verbose_name_plural = "Ubicaciones"


class Sucursal(models.Model):

    nombre = models.CharField(max_length = 50)
    ubicacion = models.ForeignKey(Ubicacion)
    telefono = models.IntegerField()

    class Meta:
        verbose_name_plural = "Sucursales"


class Cargo(models.Model):

    nombre = models.CharField(max_length = 50)
    sueldo = models.IntegerField()

    def __unicode__(self):
        return self.nombre


class Empleado(models.Model):

    nombre = models.CharField(max_length = 50)
    cargo = models.ForeignKey(Cargo)
    telefono = models.IntegerField()
    cedula = models.IntegerField()
    sucursal = models.ForeignKey(Sucursal)
