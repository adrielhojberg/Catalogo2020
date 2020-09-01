from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import AltaProducto
from .models import Producto

# VISTA BASADA EN FUNCIONES
def Listar(request):
	return render(request,'productos/listar.html')


# VISTAS BASADAS EN CLASES
class Crear(CreateView):
	model = Producto
	form_class = AltaProducto
	template_name = 'productos/crear.html'
	success_url = reverse_lazy('home')
