from django.contrib import admin
from proveedor.models import Proveedor

# Register your models here.
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display =('nombre','telefono','email')
    search_fields = ('nombre','email')
    filter_horizontal = ('productos',)    
    
