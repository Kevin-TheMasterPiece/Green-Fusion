from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:ID_ensalada>/<str:precio_base>/<str:tamaño>/', views.cart_add, name='cart_add'),
    path('remove/<int:ID_ensalada>/', views.cart_remove,
                                     name='cart_remove'),
]