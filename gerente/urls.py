from django.urls import path
from .views import iniciar_sesion, mostrar_empleados,reportes

urlpatterns = [
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('reportes/', reportes, name='reportes'),
    path('mostrar_empleados/', mostrar_empleados, name='mostrar_empleados'),
]


