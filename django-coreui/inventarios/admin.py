from django.contrib import admin
from .models import TipoMovimiento,MovimientoInventario


# Register your models here.
@admin.register(TipoMovimiento)
class TipoMovimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields =('nombre', )
    ordering = ('nombre',)
     
@admin.register(MovimientoInventario) 
class MovimientoInventarioAdmin(admin.ModelAdmin):
     list_display = ('fecha_movimiento','producto','tipo_movimiento','cantidad','almacen_origen','almacen_destino')  
     search_fields =('producto__nombre','tipo_movimiento__nombre', 'almacen_origen__nombre','almacen_destino__nombre')
     list_filter = ('tipo_movimiento','fecha_movimiento')
     ordering = ('fecha_movimiento',)