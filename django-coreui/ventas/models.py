from django.db import models
from vendedores.models import Vendedor
from cliente.models import Cliente
from tipo_pago.models  import TipoPago
from producto.models import Producto

class Ventas(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL,null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL,null=True)
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.SET_NULL,null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField( max_digits=10, decimal_places=2, blank=True, null=True)
    
class VentaItem(models.Model):
    venta =models.ForeignKey(Ventas, related_name='items', on_delete=models.CASCADE) 
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10,decimal_places=2)
