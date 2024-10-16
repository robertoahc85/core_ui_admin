from django.contrib import admin
from .models import TipoPago

# Register your models here.
@admin.register(TipoPago)
class TipoPagoAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','activo','es_activo')
    search_fields = ('nombre',)
    list_filter = ('activo',)
    actions = ['marcar_como_activo', 'marcar_como_inactivo']
    
    def marcar_como_activo(self,request, queryset):
        queryset.update(activo=True)
        self.message_user(request, "Los tipos de pagos selecciona han sido marcado como activos")
    
    marcar_como_activo.short_description = "Marcar como activo"
    
    def marcar_como_inactivo(self,request, queryset):
        queryset.update(activo=False)
        self.message_user(request, "Los tipos de pagos selecciona han sido marcado como inactivos")
    
    marcar_como_inactivo.short_description = "Marcar como inactivo"