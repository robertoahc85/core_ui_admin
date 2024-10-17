from django.contrib import admin
from .models import Caja

# Register your models here.
@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    list_display=('fecha_apertura', 'fecha_cierre', 'total_efectivo_inicial')
    list_filter = ('fecha_apertura', 'fecha_cierre')
    actions = ['cerrar_caja']
    
    
    def cerrar_caja(self, request, queryset):
        for caja in queryset:
            if caja.abierta:
                caja.cerrar_caja(total_efectivo_final= 1000.0)
                self.message_user(request,"Caja cerrada existosamente")
    cerrar_caja.short_description ="Cerrar Caja Selecionada"            
 