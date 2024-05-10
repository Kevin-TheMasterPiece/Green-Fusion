"""
URL configuration for Green_Fusion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gerente/', include('gerente.urls')),  # Incluye las URLs de la aplicación "gerente"
    path('administrador/', include('administrador.urls')),  # Incluye las URLs de la aplicación "administrador"
    path('preparador/', include('preparador.urls')),  # Incluye las URLs de la aplicación "preparador"
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('store.urls'))# Incluye las URLs de la aplicación "store"
    
    #FALTA MOSTRAR LAS ENSALADAS

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

