from django.shortcuts import render
from administrador.models import ingrediente
from django.contrib import messages
# Create your views here.
def pedidos (request):
    return render(request,'pedidos.html')
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
