from django.shortcuts import render
from .models import Ventas,VentasItems
from .forms import VentaForm,VentaItemForm
from django.contrib.auth.decorators import login_required

@login_required
def crear_venta(request):
    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        if venta_form.is_valid():


# Create your views here.
