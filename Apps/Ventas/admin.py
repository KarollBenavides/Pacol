from django.contrib import admin

# Register your models here.

from Apps.Ventas.models import Categoria, Producto, Cliente, Factura, Venta, Proveedor


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'nit', 'telefono', 'ubicacion']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion', 'categoria', 'proveedor']


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'cedula', 'telefono', 'direccion']


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ['id','total','producto','cliente', 'empleado']


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'empleado', 'factura']
