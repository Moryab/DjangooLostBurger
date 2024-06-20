from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    nombre=forms.CharField(max_length=25, required=True)
    
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio','categoria','imagen']