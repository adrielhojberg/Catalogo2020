
from django.contrib import admin
from django.urls import path
from . import views

app_name="productos"

urlpatterns = [
	path('/Listar/', views.ListarProductos.as_view(), name = "listar"),
	path('/Crear/', views.Crear.as_view(), name="crear"),
	path('/Modificar/<str:pk>', views.Modificar.as_view(), name="modificar"),
	path('/Eliminar/<str:pk>', views.Eliminar.as_view(), name="eliminar"),


]