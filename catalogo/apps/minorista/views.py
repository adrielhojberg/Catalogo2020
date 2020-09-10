from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import CreateView

from .forms import MinoristaForm
from apps.usuarios.models import Usuario


class RegistroMinorista(CreateView):
	model = Usuario
	form_class = MinoristaForm
	template_name = 'minorista/registro.html'
	success_url = reverse_lazy('home')