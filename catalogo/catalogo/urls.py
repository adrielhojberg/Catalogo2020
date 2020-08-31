
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="home"),
    path('Contacto',views.Contacto,name="contacto"),
    path('Login',auth.LoginView.as_view(template_name="usuarios/login.html"),name="login"),
    path('Logout',auth.LogoutView.as_view(),name="logout"),
    path('Registro',views.Registro,name="registro"),

    # URLS DE APLICACIONES
    path('Productos',include('apps.productos.urls'))
]
