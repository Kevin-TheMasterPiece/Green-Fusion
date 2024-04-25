from django.urls import path
from .views import  pedidos

urlpatterns = [
    path('pedidos/', pedidos, name='pedidos'),
]
