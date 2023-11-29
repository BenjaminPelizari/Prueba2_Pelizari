"""
URL configuration for Prueba2_Pelizari project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from prueba2_app.views import listar_socios, agregar_socio, modificar_socio, eliminar_socio, user_view, index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar/', listar_socios, name='listar_socios'),
    path('agregar/', agregar_socio, name='agregar_socio'),
    path('modificar/<int:pk>/', modificar_socio, name='modificar_socio'),
    path('eliminar/<int:pk>/', eliminar_socio, name='eliminar_socio'),
    path('user/', user_view, name='user_view'),
    path('', index, name='index'),
]
