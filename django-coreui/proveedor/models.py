from django.db import models
from producto.models import Producto

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 15)
    email = models.EmailField(unique=True)
    dirreccion = models.TextField(blank=True, null=True)
    productos = models.ManyToManyField(Producto, related_name='proveedores')
    
def __str__(self):
    return self.nombre
