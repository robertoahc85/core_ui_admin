from django.shortcuts import render,redirect
from .models import Ventas,VentasItems,Producto
from .forms import VentaForm,VentaItemForm
from django.contrib.auth.decorators import login_required

@login_required
def crear_venta(request):
    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        if venta_form.is_valid():
            venta =VentaForm.save()
            for producto_id, cantidad in zip(request.POST.getlist('producto_id')),request.POST.getlist('cantidad'):
                producto= Producto.objects.get(id=producto_id)
                VentasItems.objects.create(
                    venta=venta,
                    producto=producto,
                    cantidad = cantidad,
                    precio_unitario =producto.precio
                )
            return  redirect ('venta_exitosa', venta_id = venta.id)    


# Create your views here.
