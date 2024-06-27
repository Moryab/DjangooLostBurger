from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.contrib.auth.models import User


# Create your models here.
class Perfil(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    telefono = models.CharField(max_length=9, null=False)
    direccion = models.CharField(max_length=255, null=False)

    def __str__(self):
        return str(self.usuario)
# Tipo de producto.
CATEGORIAS = [
    ('Completos', 'Completos'),
    ('Hamburguesas', 'Hamburguesas'),
    ('Pizzas', 'Pizzas'),
    ('Papas Fritas', 'Papas Fritas'),
    ('Bebidas', 'Bebidas'),
]

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40,null=False, 
    validators=[RegexValidator(r'^[a-zA-Z ]*$', 'Ingrese solo letras y espacios.')])
    
    descripcion = models.TextField(max_length=300,null=False)
    
    precio =  models.IntegerField(validators=[MinValueValidator(0)],null=False)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='Sin Seleccionar',null=False)
    imagen = models.ImageField(upload_to='productos/',null=False)

    def __str__(self):
        return str(self.id)