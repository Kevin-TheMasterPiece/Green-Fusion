from django.urls import path
from .views import iniciar_sesion, empleados, crear_empleado, consultar_admin
from .views import buscar_empleado, editar_empleado, eliminar_empleado
urlpatterns = [
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('empleados/', empleados, name='empleados'),
    path('crear_empleado/', crear_empleado, name='crear_empleado'),
    path('consultar_admin/',consultar_admin , name='consultar_admin'),
    path('buscar_empleado/', buscar_empleado, name='buscar_empleado'),
    path('editar_empleado/', editar_empleado, name='editar_empleado'),
    path('eliminar_empleado/', eliminar_empleado, name='eliminar_empleado'),
]


