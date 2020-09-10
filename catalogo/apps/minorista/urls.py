from django.contrib import admin
from django.urls import path
from . import views

app_name="minorista"

urlpatterns = [
path('Crear/',views.RegistroMinorista.as_view(),name='registrar')
]