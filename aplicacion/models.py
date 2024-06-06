from django.db import models


# Create your models here.
class usuario(models.Model):
    id = models.CharField(max_length=8, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, null=False)
    telefono = models.CharField(max_length=9, null=False)
    direccion = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.id} - {self.nombre} {self.apellido}"