
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth

from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="home"),
    path('Contacto',views.Contacto,name="contacto"),
    path('Login',auth.LoginView.as_view(template_name="usuarios/login.html"),name="login"),
    path('Logout',auth.LogoutView.as_view(),name="logout"),

    # URLS DE APLICACIONES
    path('Productos',include('apps.productos.urls')),
    path('Usuarios',include('apps.usuarios.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
