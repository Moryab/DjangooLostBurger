from django.contrib import admin
from .models import usuario

# Register your models here.
class AdmUsuario(admin.ModelAdmin):
        list_display=['id','nombre','apellido','email','telefono','direccion']


admin.site.register(usuario, AdmUsuario)
