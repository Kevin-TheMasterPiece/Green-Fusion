from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.mostrar_ensaladas, name='mostrar_ensaladas'),
    path('<int:id>/<str:nombre_ensalada>/', views.detalles_ensalada, name='detalles_ensalada')
    #FALTA HACER BARRA DE BUSQUEDA EN INDEX
]