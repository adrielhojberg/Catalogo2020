from django.db import models

from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
	mayorista = models.BooleanField(default = False)
	pass



