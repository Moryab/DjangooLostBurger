from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ProductoForm(forms.ModelForm):
    nombre=forms.CharField(max_length=25, required=True)
    
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio','categoria','imagen']
        
class UserForm(UserCreationForm):
    pass
    class Meta:
        model=User
        fields=['username','email','password1','password2']