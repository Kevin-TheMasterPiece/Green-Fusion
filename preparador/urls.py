from django.urls import path
from .views import  pedidos, inventariopreparador

urlpatterns = [
    path('pedidos/', pedidos, name='pedidos'),
    path('inventariopreparador/', inventariopreparador, name='inventariopreparador'),
]
