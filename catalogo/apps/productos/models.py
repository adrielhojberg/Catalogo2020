from django.db import models

# Create your models here.

class Producto(models.Model):
	codigo = models.CharField(max_length = 15, primary_key = True)
	nombre = models.CharField(max_length = 80)
	descripcion = models.TextField(null = True)
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	oferta = models.BooleanField()
	imagen = models.ImageField(upload_to="productos",null = True,blank=True)

