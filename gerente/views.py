from django.shortcuts import render, redirect
from .forms import LoginForm, EmpleadoForm
from .models import empleado
from django.http import JsonResponse
from .models import empleado  # Asegúrate de importar tu modelo empleado correctamente
import base64
from django.shortcuts import get_object_or_404


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
        if form.is_valid():
            form.save()
            return redirect('empleados')  # Redirigir a la página de lista de empleados
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


        if None not in (cedula, nombreNueva, correoNueva, telefonoNueva, direccionNueva, ciudadNueva):
            try:
                # Buscar el empleado por su cédula
                empleado_obj = empleado.objects.get(cedula=cedula)
                
                # Actualizar los datos del empleado
                empleado_obj.nom_emp = nombreNueva
                empleado_obj.correo_emp = correoNueva
                empleado_obj.tel_emp = telefonoNueva
                empleado_obj.direc_emp = direccionNueva
                empleado_obj.ciudad_emp = ciudadNueva
                empleado_obj.contrasena = contrasenaNueva

                empleado_obj.save()

                # Retornar una respuesta indicando que la edición fue exitosa
                return JsonResponse({'success': True, 'message': 'Empleado actualizado correctamente'})
            except empleado.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Empleado no encontrado'}, status=404)
            except Exception as e:
                # Retornar una respuesta indicando que ocurrió un error
                return JsonResponse({'success': False, 'message': 'Se produjo un error: {}'.format(str(e))})
        else:
            # Retornar una respuesta indicando que falta algún parámetro
            return JsonResponse({'error': 'Faltan parámetros en la solicitud'}, status=400)
    else:
        # Retornar una respuesta indicando que el método no está permitido
        return JsonResponse({'error': 'Método no permitido'}, status=405)
