from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.mostrar_ensaladas, name='mostrar_ensaladas'),
    path('<int:ID_ensalada>/<str:nombre_ensalada>/', views.detalles_ensalada, name='detalles_ensalada'),
    path('personalizada/', views.armar_ensalada, name='personalizada')
    #FALTA HACER BARRA DE BUSQUEDA EN INDEX
]