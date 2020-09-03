from django import forms

from .models import Producto

class AltaProducto(forms.ModelForm):

	class Meta:
		model = Producto
		fields = '__all__'

class ModificacionProducto(forms.ModelForm):

	class Meta:
		model = Producto
		fields = ['nombre','descripcion','precio']