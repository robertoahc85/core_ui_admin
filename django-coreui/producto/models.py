from django.db import models
from categoria.models import Categoria

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

