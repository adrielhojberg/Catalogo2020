
from django.contrib.auth.forms import UserCreationForm

from apps.usuarios.models import Usuario
from .models import Minorista
from django import forms
from django.db import transaction
class MinoristaForm(UserCreationForm):
	edad = forms.IntegerField()

	class Meta:
		model = Usuario
		fields =['username','email','first_name','last_name','password1','password2']

	@transaction.atomic
	def save(self):
		usuario = super().save(commit = False)
		usuario.mayorista = False
		usuario.save()
		Minorista.objects.create(usuario= usuario, edad =  self.cleaned_data.get('edad'))
		
		return usuario