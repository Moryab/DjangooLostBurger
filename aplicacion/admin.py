from django.contrib import admin
from .models import Perfil, Producto, Pedido, DetallePedido, DatosPago

# Register your models here.
class AdmPerfil(admin.ModelAdmin):
        list_display=['telefono','direccion','prefijo_telefono']


class AdmProducto(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion','precio','categoria','imagen']

class AdmPedido(admin.ModelAdmin):
    list_display = ['id_pedido', 'cliente', 'rut', 'fecha', 'direccion', 'telefono', 'total', 'estado']
    list_filter = ['estado', 'fecha']
    search_fields = ['cliente__username', 'rut', 'direccion']
    date_hierarchy = 'fecha'

class AdmDetallePedido(admin.ModelAdmin):
    list_display = ['id', 'pedido', 'producto', 'cantidad', 'subtotal', 'precio_unitario']
    list_filter = ['pedido', 'producto']
    search_fields = ['pedido__id_pedido', 'producto__nombre']

admin.site.register(Producto, AdmProducto)
admin.site.register(Perfil, AdmPerfil)
admin.site.register(Pedido, AdmPedido)
admin.site.register(DetallePedido, AdmDetallePedido)
admin.site.register(DatosPago)