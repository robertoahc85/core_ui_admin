from django.contrib import admin
from cliente.models import Cliente

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nombre', 'apellido', 'email', 'telefono')
    search_fields=('nombre', 'apellido','email' )
    list_filter= ('nombre','apellido')
    ordering =('apellido', 'nombre')