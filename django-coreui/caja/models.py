from django.db import models
from django.utils import timezone

# Create your models here.
class Caja(models.Model):
    fecha_apertura = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    abierta = models.BooleanField(default=True)
    total_efectivo_inicial = models.DecimalField(max_digits=10,decimal_places=2)
    total_efectivo_final = models.DecimalField(max_digits=10,decimal_places=2)
    
    def cerrar_caja(self, total_efectivo_final):
        self.total_efectivo_final = total_efectivo_final
        self.fecha_cierre = timezone.now()
        self.abierta = False
        self.save()
        
        
    def __str__(self):
        estado= "abierta" if self.abierta else "cerrada"
        return f"Caja{estado} - Apertura: {self.fecha_apertura}"