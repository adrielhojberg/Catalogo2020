from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import CreateView

from .forms import RegistroUsuarioForm
from .models import Usuario

