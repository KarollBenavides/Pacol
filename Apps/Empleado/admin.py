from django.contrib import admin
from models import Cargo, Empleado, Sucursal, Ubicacion, Pais, Ciudad, Departamento
# Register your models here.

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'sueldo']


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'cedula', 'telefono', 'cargo']


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'pais']


@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'departamento']


@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'direccion', 'ciudad']


@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'ubicacion']
