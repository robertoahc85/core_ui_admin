from django import forms
from .models import Ventas, VentaItem

class VentaForm(forms.ModelForm):
    class Meta:
        model = Ventas  # Cambia 'models' a 'model'
        fields = ['vendedor', 'cliente', 'tipo_pago','total']

class VentaItemForm(forms.ModelForm):
    class Meta:
        model = VentaItem  # Cambia 'models' a 'model'
        fields = ['producto', 'cantidad', 'precio_unitario']