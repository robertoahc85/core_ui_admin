from django.db import models
from vendedores.models import Vendedor
from cliente.models import Cliente
from tipo_pago.models import TipoPago
from producto.models import Producto
from inventarios.models import MovimientoInventario, TipoMovimiento

import logging
# Configura el logger
logger = logging.getLogger(__name__)

class Ventas(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def calcular_total(self):  #Calcula el total sumando los subtotales de todos los ítems de la venta.
        total = sum(item.subtotal() for item in self.items.all())
        return total
    
    
    def save(self, *args, **kwargs):
    # Guarda la venta, primero sin calcular el total.
        #Luego guarda los ítems y recalcula el total.
        if not self.pk:  # Si la venta aún no tiene una clave primaria (es nueva)
            super().save(*args, **kwargs)  # Guardar la venta primero sin total
        try:
            # Una vez que la venta ya tiene una clave primaria, calculamos el total
            self.total = self.calcular_total()
            super().save(*args, **kwargs)  # Guardar nuevamente, ahora con el total actualizado
        except Exception as e:
            logger.error(f"Error al guardar la venta: {e}")
            raise

    def __str__(self):
        return f"Venta {self.id} - Total: {self.total}"


class VentaItem(models.Model):
    venta = models.ForeignKey(Ventas, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        #Retorna el subtotal del ítem.
        return self.cantidad * self.precio_unitario

    def save(self, *args, **kwargs):
        #Guarda el ítem y actualiza el total de la venta asociada.
        super().save(*args, **kwargs)
        # Después de guardar el ítem, recalculamos el total de la venta
        self.venta.save()
        self.actualizar_stock()
        
    
    def actualizar_stock(self):
        cantidad_actual = int(self.cantidad)
        stock_actual = int(self.producto.stock)
        if stock_actual >= cantidad_actual:
            self.producto.stock-= cantidad_actual
            self.producto.save()
        else:
            logger.error(f"El stock es menor a lo solicitado")  
        #Agregar movimientos_inventario      
        tipo_movimiento = TipoMovimiento.objects.get(nombre='salidas')
        movimiento = MovimientoInventario(
            producto = self.producto,
            tipo_movimiento =tipo_movimiento,
            cantidad = cantidad_actual,
        )  
        movimiento.save()     