from django.db import models
from apps.usuarios.models import Usuario
# Create your models here.

class Minorista(models.Model):
	usuario = models.OneToOneField(Usuario, related_name="usuario_minorista",on_delete=models.CASCADE)
	edad = models.IntegerField()



