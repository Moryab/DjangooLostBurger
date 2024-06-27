from django.contrib import admin
from .models import Perfil, Producto

# Register your models here.
class AdmPerfil(admin.ModelAdmin):
        list_display=['telefono','direccion']


class AdmProducto(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion','precio','categoria','imagen']

admin.site.register(Producto, AdmProducto)
admin.site.register(Perfil, AdmPerfil)
