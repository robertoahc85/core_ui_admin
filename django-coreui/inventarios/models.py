from django.db import models
from almacen.models import Almacen
from producto.models import  Producto
# Tipo de movimientos y  movimiento de inventario

class TipoMovimiento(models.Model):
    nombre = models.CharField(max_length=100, unique=True, choices=[
    ('entrada', 'Entrada'),
    ('salidas', 'Salida' ),  
    ('ajuste','Ajuste'),
    ('tranferencia','Tranferencia'),
    ])
    descripcion = models.TextField( blank=True , null=True)
    
    def __str__(self):
        return self.nombre

class MovimientoInventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_movimiento =models.DateTimeField(auto_now_add=True)
    

