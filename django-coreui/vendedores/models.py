from django.db import models

# Register your models here.
class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15 , blank=True , null=True)
    fecha_contratacion= models.DateField()
    
    def __str__(self):
        return self.nombre
    