from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.contrib.auth.models import User


# Create your models here.
class Perfil(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    telefono = models.CharField(max_length=9, null=False)
    direccion = models.CharField(max_length=255, null=False)
    prefijo_telefono = models.CharField(max_length=5, choices=[
        ('+56', '+56 Chile'),
        ('+34', '+34 España'),
        ('+52', '+52 México'),
        ('+54', '+54 Argentina'),
        ('+1', '+1 EE.UU.'),
        # Agrega más prefijos según sea necesario
    ])

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
    

    

class Pedido(models.Model):
    ESTADOS_PEDIDO = [
        ('Pendiente', 'Pendiente'),
        ('En camino', 'En camino'),
        ('Entregado', 'Entregado'),
        ('Cancelado', 'Cancelado'),
    ]

    id_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)  # Asumiendo que estás usando el modelo de usuario de Django para los clientes
    rut = models.CharField(max_length=12)  # Asegúrate de tener una validación adecuada para el RUT
    fecha = models.DateField(auto_now_add=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10, choices=ESTADOS_PEDIDO, default='Pendiente')


    def __str__(self):
        return f'Pedido {self.id_pedido} - {self.cliente}'
    
class DatosPago(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='datos_pago')
    rut = models.CharField(max_length=12)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    prefijo_telefono = models.CharField(max_length=5, choices=[
        ('+56', '+56 Chile'),
        ('+34', '+34 España'),
        ('+52', '+52 México'),
        ('+54', '+54 Argentina'),
        ('+1', '+1 EE.UU.'),
        # Agrega más prefijos según sea necesario
    ])

    def __str__(self):
        return f"Datos de Pago para {self.pedido}" 

class DetallePedido(models.Model):
    pedido = models.ForeignKey('Pedido', related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Detalle del Pedido {self.pedido.id_pedido} - Producto: {self.producto.nombre}'
    
    @property
    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad
