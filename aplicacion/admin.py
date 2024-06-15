from django.contrib import admin
from .models import usuario, Producto

# Register your models here.
class AdmUsuario(admin.ModelAdmin):
        list_display=['id','nombre','apellido','email','telefono','direccion']


class AdmProducto(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion','precio','categoria','imagen']

admin.site.register(Producto, AdmProducto)
admin.site.register(usuario, AdmUsuario)
