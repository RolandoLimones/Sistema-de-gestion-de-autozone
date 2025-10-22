from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'cantidad', 'proveedor_id', 'precio', 'almacen_id', 'foto']
        labels = {
            'nombre_producto': 'Nombre del producto',
            'cantidad': 'Cantidad',
            'proveedor_id': 'Proveedor ID',
            'precio': 'Precio',
            'almacen_id': 'Almacen ID',
            'foto': 'Foto'
        }
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'proveedor_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'almacen_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }