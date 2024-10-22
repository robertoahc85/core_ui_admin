from django.shortcuts import render,redirect
from .models import Ventas,VentaItem,Producto
from .forms import VentaForm,VentaItem
from django.contrib.auth.decorators import login_required

@login_required
def crear_venta(request):
    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        if venta_form.is_valid():
            venta = venta_form.save()
            
            producto_ids = request.POST.getlist('producto_id') 
            cantidades = request.POST.getlist('cantidad') 
            
            for producto_id, cantidad in zip(producto_ids, cantidades): 
                producto= Producto.objects.get(id=producto_id)
                VentaItem.objects.create(
                    venta=venta,
                    producto=producto,
                    cantidad = cantidad,
                    precio_unitario =producto.precio
                )
            return  redirect ('venta_exitosa', venta_id = venta.id) 
    else:
          venta_form = VentaForm()     
    
    productos = Producto.objects.filter(stock__gt=0) #greater than 
    return render (request, 'ventas/crear_venta.html',{'venta_form' : venta_form, 'productos' : productos})



# Create your views here.
def venta_exitosa(request, venta_id):
    venta = Ventas.objects.get(id=venta_id)
    return render(request, 'ventas/venta_exitosa.html', {'venta' : venta})