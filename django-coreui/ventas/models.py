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
    
    def calcular_total(self):
        total = sum(items.subtotal() for items in self.items.all)
        return total
    
    def save(self, *args, **kwarg ):
            self.total = self.calcular_total()
            super().save( *args, **kwarg )
         
    def  __str__(self):
        return f" Venta {self.id}"   
    
    
class VentaItem(models.Model):
    venta =models.ForeignKey(Ventas, related_name='items', on_delete=models.CASCADE) 
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10,decimal_places=2)
    
    def  subtotal (self):
        return self.cantidad * self.precio_unitario
    
    
#TODO   QUE DESCUENTE DEL INVENTARIOS