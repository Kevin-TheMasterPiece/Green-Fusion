from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.mostrar_ensaladas, name='mostrar_ensaladas'),
    path('<int:ID_ensalada>/<str:nombre_ensalada>/', views.detalles_ensalada, name='detalles_ensalada'),
    path('personalizada/', views.armar_ensalada, name='personalizada'),
    path('reclamos/', views.crear_reclamo, name='crear_reclamo'),
    #path('login/', views.login, name='login'),
    path('exit/', views.exit, name='exit'),
    path('reclamos/<int:reclamo_id>/borrar/', views.borrar_reclamo, name='borrar_reclamo'),
    path('register/', views.registrer, name='registrer'),
    #FALTA HACER BARRA DE BUSQUEDA EN INDEX
]