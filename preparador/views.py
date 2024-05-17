from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from administrador.models import ingrediente
from django.contrib import messages
from store.models import factura, ensaladas
# Create your views here.
def pedidos (request, pedido_id= None):
    pedido = None
    pedidos = factura.objects.filter(preparada=False)
    ensaladas_pedido = []
    ingredientes = []

    for pedid in pedidos:
        for ensalada in pedid.items.all():
            ensaladas_pedido.append(ensalada)
            ingredientes.extend(ensalada.FK_ensalada.ingredientes.all())

    total_ensaladas = len(ensaladas_pedido)

    if pedido_id:
         pedido = factura.objects.filter(id=pedido_id)
    
    return render(request, 'pedidos.html', {
        'pedidos': pedidos,
        'ensaladas_pedido': ensaladas_pedido,
        'total_ensaladas': total_ensaladas,
        'ingredientes': ingredientes,
        'pedido': pedido,
    })





def inventariopreparador (request):
    ingredientes = ingrediente.objects.all()
    return render(request,'inventariopreparador.html', {'ingredientes': ingredientes})

def modificar_ingrediente(request):
    if request.method == 'POST':
        ingrediente_id = request.POST['ingrediente']
        cantidad = float(request.POST['cantidad'])
        
        ingrediente_seleccionado = ingrediente.objects.get(ID_ing=ingrediente_id)
        
        ingrediente_seleccionado.cant_gramos -= cantidad
        ingrediente_seleccionado.save()

        messages.success(request, 'Modificación exitosa')

    ingredientes = ingrediente.objects.all()

    return render(request, 'inventariopreparador.html', {'ingredientes': ingredientes})
