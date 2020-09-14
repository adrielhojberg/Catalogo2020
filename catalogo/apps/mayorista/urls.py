from django.contrib import admin
from django.urls import path
from . import views

app_name="mayorista"

urlpatterns = [
path('Crear/',views.RegistroMayorista.as_view(),name='registrar')
]