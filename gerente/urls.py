from django.urls import path
from .views import iniciar_sesion, empleados, crear_empleado

urlpatterns = [
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('empleados/', empleados, name='empleados'),
    path('crear_empleado/', crear_empleado, name='crear_empleado'),
]


