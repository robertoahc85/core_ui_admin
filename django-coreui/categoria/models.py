from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=1000, unique=True)
    descripcion =models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre