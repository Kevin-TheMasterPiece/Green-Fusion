from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from administrador.models import ensaladas, ingrediente
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from .models import reclamo
from .forms import ReclamoForm, CustomUserCreationForm
from django.utils import timezone
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

def mostrar_ensaladas (request, busqueda_nombre = None):#Va a mostrar las ensaldas
    ensalada_enc = None
    ensalada = ensaladas.objects.filter(activo = True)
    if busqueda_nombre:#Si hay una busqueda va a hacer el filtro y mostrar la ensalda a buscar
        ensalada_enc = get_object_or_404(ensaladas, nom_ensalada = busqueda_nombre)
        ensalada = ensalada.filter(nom_ensalada = ensalada_enc)
    
    return render(request, 'index.html', 
                  {'ensalada_enc': ensalada_enc,
                   'ensalada': ensalada})

def detalles_ensalada (request, ID_ensalada, nombre_ensalada):
    ensalada_detalle = get_object_or_404(ensaladas, ID_ensalada = ID_ensalada, nom_ensalada = nombre_ensalada, activo = True)
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

    cart_product_form = CartAddProductForm()

    return render(request, 'ensalada.html',
                  {'ensalada_detalle': ensalada_detalle,
                   'ingredientes' : ingredientes,
                   'precio_base': precio_base,
                   'tamaño': tamaño,
                   'peso': peso,
                   'cart_product_form': cart_product_form})

def armar_ensalada(request):

    frutas = ingrediente.objects.filter(categoria = 'Frutas')
    vegetales = ingrediente.objects.filter(categoria= 'Vegetales')

    contexto = {
        'frutas': frutas,
        'vegetales': vegetales
    }

    return render(request, 'personalizada.html', contexto)

@login_required
def crear_reclamo(request):
    if request.method == 'POST':
        form = ReclamoForm(request.POST, request.FILES)
        if form.is_valid():
            reclamo_obj = form.save(commit=False)
            # Asignar la fecha actual
            reclamo_obj.fecha_reclamo = timezone.now().date()
            # Asignar el cliente a la llave foránea
            reclamo_obj.FK_ced_client = request.user
            # Guardar el reclamo
            reclamo_obj.save()
            return redirect('store:crear_reclamo')
    else:
        form = ReclamoForm()

    # Obtén los reclamos del usuario actual
    reclamos_usuario = reclamo.objects.filter(FK_ced_client=request.user)



    return render(request, 'crear_reclamo.html', {'form': form,
                                                  'reclamos_usuario': reclamos_usuario})

def borrar_reclamo(request, reclamo_id):
    reclamo_obj = get_object_or_404(reclamo, pk=reclamo_id)
    if request.method == 'POST':
        reclamo_obj.delete()
        return redirect('store:crear_reclamo')
    return render(request, 'crear_reclamo.html', {'reclamo_borrar': reclamo_obj})


#def login (request):
    #return render(request, 'registration/login.html')

def exit (request):
    logout(request)
    return redirect('store:mostrar_ensaladas')

def registrer (request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('store:mostrar_ensaladas')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)
