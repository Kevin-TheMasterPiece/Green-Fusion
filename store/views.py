from decimal import Decimal
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
    ingredientes = ensalada_detalle.ingredientes.all()

    # Inicializa el tamaño en 'pequeña' como valor predeterminado
    tamaño = 'pequeña'
    
    # Si es una solicitud POST, obtén el tamaño seleccionado por el usuario
    if request.method == 'GET':
        tamaño = request.GET.get('tamaño', 'disabled')
    
    # Calcula el precio base de la ensalada
    precio_base = sum(ingrediente.precio_min for ingrediente in ingredientes)
    #Calcula el peso base de la ensalada
    peso = sum(ingrediente.cant_min for ingrediente in ingredientes)

    # Ajusta el precio base según el tamaño seleccionado
    if tamaño == 'mediana':
        precio_base *= 2 
        peso *= 2
    elif tamaño == 'grande':
        precio_base *= 3 
        peso *= 3
#mostrar cuanto pesa la ensalada
    return render(request, 'ensalada.html',
                  {'ensalada_detalle': ensalada_detalle,
                   'ingredientes' : ingredientes,
                   'precio_base': precio_base,
                   'tamaño': tamaño,
                   'peso': peso})

