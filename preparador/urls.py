from django.urls import path
from .views import  pedidos, inventariopreparador, modificar_ingrediente

urlpatterns = [
    path('pedidos/', pedidos, name='pedidos'),
    path('inventariopreparador/', inventariopreparador, name='inventariopreparador'),
    path('modificar_ingrediente/', modificar_ingrediente, name='modificar_ingrediente'),

]
