from django.db.models.signals  import post_save
from django.dispatch import receiver
from .models import MovimientoInventario
from .models import Producto

@receiver(post_save, sender=MovimientoInventario)
def actualizar_stock(sender,instance, created, **kwargs):
    if created:
        producto = instance.producto
        cantidad = instance.cantidad
        
        if instance.tipo_movimiento.nombre == 'entrada':
            producto.stock += cantidad
        elif instance.tipo_movimiento.nombre == 'salidas':
            producto.stock -= cantidad
            
    producto.save() 
    
 