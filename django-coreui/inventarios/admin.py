from django.contrib import admin
from .models import TipoMovimiento


# Register your models here.
@admin.register(TipoMovimiento)
class TipoMovimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields =('nombre', )
    ordering = ('nombre',)