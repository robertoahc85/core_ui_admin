from django.contrib import admin
from proveedor.models import Proveedor

# Register your models here.
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display =('nombre','telefono','email', 'mostrar_producto')
    search_fields = ('nombre','email')
    filter_horizontal = ('productos',)    
    
    def mostrar_producto(self,obj):
        return ", ". join([producto.nombre for producto in obj.productos.all()])
    mostrar_producto.short_description = "Productos"
