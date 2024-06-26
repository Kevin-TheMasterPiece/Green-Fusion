import os
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, EmpleadoForm
from .models import empleado
from django.http import JsonResponse
from administrador.models import recetas,ensaladas, product_prov,proveedor, ingrediente
import base64
from django.contrib import messages
from store.models import reclamo


def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cedula = form.cleaned_data['cedula']  # Obtén la cédula del formulario
            contrasena = form.cleaned_data['contrasena']  # Obtén la contraseña del formulario
            try:
                empleado_existente = empleado.objects.get(cedula=cedula)  # Busca el empleado por cédula
                if empleado_existente.contrasena == contrasena:
                    if empleado_existente.FK_ID_Rol_id == 0: #INICIO GERENTE
                        return redirect('empleados')  # Redirige si la contraseña coincide
                    elif empleado_existente.FK_ID_Rol_id == 1: #INICIO ADMINISTRADOR
                        return redirect('Vista_Admin')  # Redirige si la contraseña coincide
                    elif empleado_existente.FK_ID_Rol_id == 2: #INICIO PREPARADOR
                        return redirect('pedidos')  # Redirige si la contraseña coincide
                else:
                    # Contraseña incorrecta
                    return render(request, 'iniciar_sesion.html', {'form': form, 'error_message': 'Contraseña incorrecta'})
            except empleado.DoesNotExist:
                # Empleado no encontrado
                return render(request, 'iniciar_sesion.html', {'form': form, 'error_message': 'Empleado no encontrado'})
    else:
        form = LoginForm()
    return render(request, 'iniciar_sesion.html', {'form': form})
def empleados(request):
    empleados = empleado.objects.all()
    return render(request, 'empleados.html', {'empleados': empleados})


def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES)
        cedula = form.data.get('cedula')  # Cambia de cleaned_data a data
        if empleado.objects.filter(cedula=cedula).exists():
            messages.error(request, 'La cédula ya está registrada.')
            form = EmpleadoForm(request.POST, request.FILES)
        elif form.is_valid():
            form.save()
            return redirect('empleados')
        else:
            messages.error(request, 'Hubo un error al procesar el formulario. Por favor, revise los datos e inténtelo de nuevo.')
    else:
        form = EmpleadoForm()
    return render(request, 'crear_empleado.html', {'form': form})

def consultar_admin(request):
    return render(request, 'consultar_admin.html')

def buscar_empleado(request):
    if request.method == 'GET' and 'cedula' in request.GET:
        cedula = request.GET['cedula']
        try:
            empleado_obj = empleado.objects.get(cedula=cedula)
            foto_data = None
            if empleado_obj.foto_emp:
                with open(empleado_obj.foto_emp.path, 'rb') as f:
                    foto_data = base64.b64encode(f.read()).decode('utf-8')  # Codifica la imagen a base64 y convierte los bytes a cadena UTF-8

            data = {
                'nombre': empleado_obj.nom_emp,
                'cedula': empleado_obj.cedula,
                'correo': empleado_obj.correo_emp,
                'telefono': empleado_obj.tel_emp,
                'direccion': empleado_obj.direc_emp,
                'ciudad': empleado_obj.ciudad_emp,
                'contrasena': empleado_obj.contrasena,
                'foto_data': foto_data,
            }
            return JsonResponse(data)
        except empleado.DoesNotExist:
            return JsonResponse({'error': 'Empleado no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def editar_empleado(request):
    if request.method == 'GET':
        # Obtener los datos del formulario
        cedula = request.GET.get('cedula')
        nombreNueva = request.GET.get('nombre')
        correoNueva = request.GET.get('correo')
        telefonoNueva = request.GET.get('telefono')
        direccionNueva = request.GET.get('direccion')
        ciudadNueva = request.GET.get('ciudad')
        contrasenaNueva = request.GET.get('contrasena')
        
        try:
                # Buscar el empleado por su cédula
                empleado_obj = empleado.objects.get(cedula=cedula)

                # Verificar si algún campo nuevo es None o una cadena vacía
                if nombreNueva is not None and nombreNueva.strip() != '':
                    empleado_obj.nom_emp = nombreNueva
                if correoNueva is not None and correoNueva.strip() != '':
                    empleado_obj.correo_emp = correoNueva
                if telefonoNueva is not None and telefonoNueva.strip() != '':
                    empleado_obj.tel_emp = telefonoNueva
                if direccionNueva is not None and direccionNueva.strip() != '':
                    empleado_obj.direc_emp = direccionNueva
                if ciudadNueva is not None and ciudadNueva.strip() != '':
                    empleado_obj.ciudad_emp = ciudadNueva
                if contrasenaNueva is not None and contrasenaNueva.strip() != '':
                    empleado_obj.contrasena = contrasenaNueva

                empleado_obj.save()  # Guardar los cambios en la base de datos
                # Retornar una respuesta indicando que la edición fue exitosa
                return redirect('empleados')  # Redirigir a la página de lista de empleados
        except empleado.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'El empleado no existe'})
        except Exception as e:
            return JsonResponse({'Error': 'Se produjo un error'}, status=404)
    else:
        return JsonResponse({'Error': 'Método no permitido'}, status=405)
    

def eliminar_empleado(request):
    if request.method == 'GET':
        cedula = request.GET.get('cedula')  # Obtener la cédula del empleado a eliminar
        try:
            # Buscar el empleado por su cédula
            empleado_obj = empleado.objects.get(cedula=cedula)
            
            # Eliminar el archivo de imagen si existe
            if empleado_obj.foto_emp:
                ruta_imagen = empleado_obj.foto_emp.path
                if os.path.exists(ruta_imagen):
                    os.remove(ruta_imagen)
            
            # Eliminar el objeto empleado de la base de datos
            empleado_obj.delete()
            
            return JsonResponse({'success': True, 'message': 'Empleado eliminado correctamente'})
        except empleado.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'El empleado no existe'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
def mostrar_reclamoo(request):
    reclamos_usuario = reclamo.objects.filter(FK_ced_client=request.user)
    return render(request, 'mostrar_reclamo_gerente.html', {'reclamos_usuario': reclamos_usuario})
                                                  
def borrar_reclamo(request, reclamo_id):
    reclamo_obj = get_object_or_404(reclamo, pk=reclamo_id)
    if request.method == 'POST':
        reclamo_obj.delete()
        return redirect('mostrar_reclamo_gerente.html')
    return render(request, 'mostrar_reclamo_gerente.html', {'reclamo_borrar': reclamo_obj})

def directorio(request):
    ingredientes = ingrediente.objects.all()
    receta= recetas.objects.all()
    ensalada= ensaladas.objects.all()
    product_provs= product_prov.objects.all()
    proveedores = proveedor.objects.all()
    return render(request, 'ver_inventario.html', {'ingredientes': ingredientes, 'product_provs':product_provs,  'proveedores': proveedores, 'receta':receta,  'ensalada': ensalada})
