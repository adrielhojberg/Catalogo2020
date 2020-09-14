from django.contrib.auth.forms import UserCreationForm
from apps.usuarios.models import Usuario
from django import forms
from django.db import transaction
from .models import Mayorista

class MayoristaForm(UserCreationForm):
	cuit = forms.IntegerField()
	razon = forms.CharField(max_length=100)

	class Meta:
		model = Usuario
		fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

	@transaction.atomic
	def save(self):
		usuario = super().save(commit=False)
		usuario.mayorista = True
		usuario.save()
		Mayorista.objects.create(usuario = usuario, cuit = self.cleaned_data.get('cuit'),
									razon = self.cleaned_data.get('razon'))
		return usuario