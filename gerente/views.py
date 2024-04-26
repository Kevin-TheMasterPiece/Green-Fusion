from django.shortcuts import render, redirect
from .forms import LoginForm, EmpleadoForm
from .models import empleado

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
