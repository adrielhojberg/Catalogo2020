from django.db import models
from apps.usuarios.models import Usuario
# Create your models here.

class Mayorista(models.Model):
	usuario = models.OneToOneField(Usuario, related_name="usuario_mayorista",on_delete=models.CASCADE)
	cuit = models.IntegerField()
	razon = models.CharField(max_length=100)


	