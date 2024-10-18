from django import forms
from .models import Ventas,VentaItem

class VentaForm(forms.ModelForm):
    class Meta:
        models = Ventas
        fields = ['vendedor','cliente','tipo_pago']

class VentaItemForm(forms.ModelForm):
    class Meta:
        models = VentaItem
        fields = ['producto','cantidad','precio_unitario']        