from django.db import models

class TipoPago(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True ,null=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    def es_activo(self):
        return "Si" if self.activo else "No"
    es_activo.short_description = "Activo"
