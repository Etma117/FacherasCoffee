import json
from django.contrib import admin
from django import forms
from django.forms import CharField
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__' #nombre, descripcion, sabores_raw, precio, categoria, imagen 
        labels = {
            'nombre': 'Nombre del Platillo o Bebida',
            'descripcion': 'Descripción breve',
            'sabores_raw': 'Sabores: inserte los sabores separados por una coma.',
            'precio':'Precio Unitario',
            'categoria':'Categoria',
            'imagen':'Imagen Representativa'
        }
        widgets ={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class': 'form-control'}),
            'sabores_raw': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-input'}),            
            'precio' : forms.NumberInput(attrs={'class': 'form-control'}),            
            'imagen' : forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg', 
                                                       'id':'formFileLg' })
        }

   
     
class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm
