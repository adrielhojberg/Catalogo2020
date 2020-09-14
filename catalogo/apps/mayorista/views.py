from django.shortcuts import render
from django.views.generic import CreateView
from .forms import MayoristaForm
from .models import Usuario
from django.urls import reverse_lazy
# Create your views here.

class RegistroMayorista(CreateView):
	model = Usuario
	form_class = MayoristaForm
	template_name = 'mayorista/registro.html'
	success_url = reverse_lazy('home')