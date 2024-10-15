from django.contrib import admin
from .models import Producto



# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock','categoria')
    search_fields = ('nombre','categoria_nombre')
    list_filter =('categoria',)
    ordering = ('nombre', )
    
    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['nombre']
        return super().get_readonly_fields(request, obj)