from django.shortcuts import render, get_object_or_404
from administrador.models import ensaladas

def mostrar_ensaladas (request, busqueda_nombre = None):#Va a mostrar las ensaldas
    ensalada_enc = None
    ensalada = ensaladas.objects.filter(activo = True)
    if busqueda_nombre:#Si hay una busqueda va a hacer el filtro y mostrar la ensalda a buscar
        ensalada_enc = get_object_or_404(ensaladas, nom_ensalada = busqueda_nombre)
        ensalada = ensalada.filter(nom_ensalada = ensalada_enc)
    
    return render(request, 'index.html', 
                  {'ensalada_enc': ensalada_enc,
                   'ensalada': ensalada})

def detalles_ensalada (request, id, nombre_ensalada):
    ensalada_detalle = get_object_or_404(ensaladas, ID_ensalada = id, nom_ensalada = nombre_ensalada, activo = True)

    return render(request, 'ensalada.html',
                  {'ensalada_detalle': ensalada_detalle})

