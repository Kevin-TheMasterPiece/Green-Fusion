"""
URL configuration for Green_Fusion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from .views import  Vista_Admin, consultar_prep, crear_prep, Modificar_prep, buscar_preparador, editar_preparador, eliminar_preparador

urlpatterns = [
    path('Vista_Admin/', Vista_Admin, name='Vista_Admin'),
    path('consultar_prep/', consultar_prep, name='consultar_prep'),
    path('crear_prep/', crear_prep, name='crear_prep'),
    path('Modificar_prep/', Modificar_prep, name='Modificar_prep'),
    path('buscar_empleado/', buscar_preparador, name='buscar_empleado'),
    path('editar_empleado/', editar_preparador, name='editar_empleado'),
    path('eliminar_empleado/', eliminar_preparador, name='eliminar_empleado'),

]


