from django.shortcuts import render


def Home(request):
	u = request.user
	#if u.mayorista:
	#	print(u.usuario_mayorista.cuit)
	return render(request,'home.html')

def Contacto(request):
	return render(request,'contacto.html')


