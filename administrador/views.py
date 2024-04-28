import os
from django.shortcuts import render, redirect
from .forms import  PreparadorForm
from gerente.models import empleado 
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
import base64


# Create your views here.
def Vista_Admin (request):
    return render(request,'Vista_Admin.html')

def crear_prep(request):
    if request.method == 'POST':
        form = PreparadorForm(request.POST, request.FILES)
        cedula = form.data.get('cedula')  # Cambia de cleaned_data a data
        if empleado.objects.filter(cedula=cedula).exists():
            messages.error(request, 'La cédula ya está registrada.')
            form = PreparadorForm(request.POST, request.FILES)
        elif form.is_valid():
            form.save()
            return redirect('consultar_prep')
        else:
            messages.error(request, 'Hubo un error al procesar el formulario. Por favor, revise los datos e inténtelo de nuevo.')
    else:
        form = PreparadorForm()
    return render(request, 'Registro.Prep.html', {'form': form})

def consultar_prep(request):
    
    empleados = empleado.objects.all()
    return render(request, 'listadoprep.html', {'empleados': empleados})
def Modificar_prep(request):
    return render(request, 'Modificar.prep.html')

def buscar_preparador(request):
    if request.method == 'GET' and 'cedula' in request.GET:
        cedula = request.GET['cedula']
        try:
            # Filtra los empleados cuya llave foránea FK_ID_Rol tenga un id igual a 2
            empleado_obj = empleado.objects.filter(cedula=cedula, FK_ID_Rol__id=2).first()
            if empleado_obj:
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
            else:
                return JsonResponse({'error': 'Empleado no encontrado'}, status=404)
        except Empleado.DoesNotExist:
            return JsonResponse({'error': 'Empleado no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def editar_preparador(request):
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
                return redirect('consultar_prep')  # Redirigir a la página de lista de empleados
        except empleado.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'El empleado no existe'})
        except Exception as e:
            return JsonResponse({'Error': 'Se produjo un error'}, status=404)
    else:
        return JsonResponse({'Error': 'Método no permitido'}, status=405)
    



def eliminar_preparador(request):
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
