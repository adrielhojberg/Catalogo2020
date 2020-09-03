from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .forms import AltaProducto, ModificacionProducto
from .models import Producto

# VISTA BASADA EN FUNCIONES
#def Listar(request):
#	return render(request,'productos/listar.html')


# VISTAS BASADAS EN CLASES
class Crear(CreateView):
	model = Producto
	form_class = AltaProducto
	template_name = 'productos/crear.html'
	success_url = reverse_lazy('home')

class Modificar(UpdateView):
	model = Producto
	form_class = ModificacionProducto
	template_name = 'productos/modificar.html'
	success_url = reverse_lazy('home')

class ListarProductos(ListView):
	model = Producto
	template_name = 'productos/listar.html'

class Eliminar(DeleteView):
	model = Producto
	success_url = reverse_lazy('productos:listar')