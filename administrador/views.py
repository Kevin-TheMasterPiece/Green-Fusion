import os
from django.shortcuts import render, redirect, get_object_or_404
from .forms import  PreparadorForm, ProveedorForm, IngredienteForm
from gerente.models import empleado
from .models import proveedor, ingrediente, product_prov, ensaladas, recetas
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
import base64
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from store.models import reclamo


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
        except empleado.DoesNotExist:
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

def crear_prov(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST, request.FILES)  # Utiliza ProveedorForm en lugar de PreparadorForm
        nit = form.data.get('nit')
        if proveedor.objects.filter(nit=nit).exists():  # Cambia de empleado a proveedor
            messages.error(request, 'Proveedor ya registrado.')
            form = ProveedorForm(request.POST, request.FILES)  # Utiliza ProveedorForm nuevamente
        elif form.is_valid():
            form.save()
            return redirect('consultar_prov')
        else:
            messages.error(request, 'Hubo un error al procesar el formulario. Por favor, revise los datos e inténtelo de nuevo.')
    else:
        form = ProveedorForm()  # Utiliza ProveedorForm en lugar de PreparadorForm
    return render(request, 'Registro_prov.html', {'form': form})

def consultar_prov(request):    
    proveedores = proveedor.objects.all()
    return render(request, 'listadoprov.html', {'proveedores': proveedores})
def Modificar_prov(request):
    return render(request, 'Modificar_prov.html')
def buscar_prov(request):
    if request.method == 'GET' and 'nit' in request.GET:
        nit = request.GET['nit']
        try:
            proveedor_obj = proveedor.objects.get(nit=nit)

            data = {
                'nit': proveedor_obj.nit,
                'nom_prov': proveedor_obj.nom_prov,
                'correo_prov': proveedor_obj.correo_prov,
                'tel_prov': proveedor_obj.tel_prov,
                'ciudad_prov': proveedor_obj.ciudad_prov,
                'desc_prov': proveedor_obj.desc_prov,
            }
            return JsonResponse(data)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Proveedor no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
def editar_prov(request):
    if request.method == 'GET':
        nit = request.GET.get('nit')
        nombre = request.GET.get('nombre_prov')
        correo = request.GET.get('correo_prov')
        telefono = request.GET.get('telefono_prov')
        ciudad = request.GET.get('ciudad_prov')
        descripcion = request.GET.get('desc_prov')

        try:
            proveedor_obj = proveedor.objects.get(nit=nit)
            if nombre:
                proveedor_obj.nom_prov = nombre
            if correo:
                proveedor_obj.correo_prov = correo
            if telefono:
                proveedor_obj.tel_prov = telefono
            if ciudad:
                proveedor_obj.ciudad_prov = ciudad
            if descripcion:
                proveedor_obj.desc_prov = descripcion

            proveedor_obj.save()
            return redirect('consultar_prov')  # Redirigir a la página de lista de empleados
        except proveedor.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Proveedor no encontrado'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def eliminar_prov(request):
    if request.method == 'GET':
        nit = request.GET.get('nit')
        try:
            proveedor_obj = proveedor.objects.get(nit=nit)
            proveedor_obj.delete()
            return JsonResponse({'success': True, 'message': 'Proveedor eliminado correctamente'})
        except proveedor.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Proveedor no encontrado'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def gestion_inventario(request):
    return render(request, 'botones2.html')
def agregar_producto(request):
    if request.method == 'POST':
        form = IngredienteForm(request.POST, request.FILES)
        ID_ing = form.data.get('ID_ing')  # Cambia de cleaned_data a data
        if ingrediente.objects.filter(ID_ing=ID_ing).exists():
            messages.error(request, 'Producto ya registrado.')
            form = IngredienteForm(request.POST, request.FILES)
        elif form.is_valid():
            form.save()
            return redirect('consultar_producto')
        else:
            messages.error(request, 'Hubo un error al procesar el formulario. Por favor, revise los datos e inténtelo de nuevo.')
    else:
        form = IngredienteForm()
    return render(request, 'agregar_producto.html', {'form': form})
def consultar_producto(request):    
    ingredientes = ingrediente.objects.all()
    return render(request, 'producto.html', {'ingredientes': ingredientes})
from django.shortcuts import HttpResponse
import json
def eliminar_producto(request):
    if request.method == 'GET':
        id_producto = request.GET.get('idProducto')
        try:
            Ingrediente = ingrediente.objects.get(ID_ing=id_producto)
            Ingrediente.delete()
            return HttpResponse(json.dumps({'success': True}), content_type='application/json')
        except ingrediente.DoesNotExist:
            return HttpResponse(json.dumps({'success': False, 'message': 'El ingrediente no existe.'}), content_type='application/json')
        except Exception as e:
            return HttpResponse(json.dumps({'success': False, 'message': str(e)}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'success': False, 'message': 'Método no permitido'}), content_type='application/json')

from django.http import JsonResponse

def editar_producto(request):
    if request.method == 'GET':
        id_producto = request.GET.get('idProducto')
        nom_ing = request.GET.get('nom_ing')
        cant_gramos = request.GET.get('cant_gramos')
        cant_min = request.GET.get('cant_min')
        precio_min = request.GET.get('precio_min')
        imagen = request.GET.get('imagen')

        try:
            ingrediente_editado = ingrediente.objects.get(ID_ing=id_producto)
            if nom_ing:
                ingrediente_editado.nom_ing = nom_ing
            if cant_gramos:
                ingrediente_editado.cant_gramos = cant_gramos
            if cant_min:
                ingrediente_editado.cant_min = cant_min
            if precio_min:
                ingrediente_editado.precio_min = precio_min
            if imagen:
                ingrediente_editado.image = imagen

            ingrediente_editado.save()
            return JsonResponse({'success': True})
        except ingrediente.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Error al editar: ingrediente no encontrado.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})


def prov_produc(request):
    ingredientes = ingrediente.objects.all()
    product_provs= product_prov.objects.all()
    proveedores = proveedor.objects.all()
    return render(request, 'prov_produc.html', {'ingredientes': ingredientes, 'product_provs':product_provs,  'proveedores': proveedores})

def eliminar_product_prov(request):
    if request.method == 'GET':
        id_producto = request.GET.get('idProducto')
        try:
            Ingrediente = product_prov.objects.get(id=id_producto)
            Ingrediente.delete()
            return HttpResponse(json.dumps({'success': True}), content_type='application/json')
        except ingrediente.DoesNotExist:
            return HttpResponse(json.dumps({'success': False, 'message': 'No existe.'}), content_type='application/json')
        except Exception as e:
            return HttpResponse(json.dumps({'success': False, 'message': str(e)}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'success': False, 'message': 'Método no permitido'}), content_type='application/json')

from django.http import JsonResponse

def editar_product_prov(request):
    if request.method == 'GET':
        id_producto = request.GET.get('idProducto')
        FK_nit_prov = request.GET.get('FK_nit_prov')
        FK_ID_ing = request.GET.get('FK_ID_ing')
        precio_prov = request.GET.get('precio_prov')
        
        try:
            ingrediente_editado = product_prov.objects.get(id=id_producto)
            if precio_prov:
                ingrediente_editado.precio_prov = precio_prov
            if FK_nit_prov:
                nuevo_proveedor = proveedor.objects.get(nit=FK_nit_prov)
                ingrediente_editado.FK_nit_prov = nuevo_proveedor
            
            if FK_ID_ing:
                nuevo_ingrediente = ingrediente.objects.get(ID_ing=FK_ID_ing)
                ingrediente_editado.FK_ID_ing = nuevo_ingrediente
            
            ingrediente_editado.save()

            return JsonResponse({'success': True})
        except ingrediente.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Error al editar: ingrediente no encontrado.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})


def agregar_product_prov(request):
    if request.method == 'GET':
        nuevo_proveedor_id = request.GET.get('proveedor')
        nuevo_ingrediente_id = request.GET.get('ingrediente')
        nuevo_precio = request.GET.get('precio')
        
        try:
            nuevo_proveedor = proveedor.objects.get(nit=nuevo_proveedor_id)
            nuevo_ingrediente = ingrediente.objects.get(ID_ing=nuevo_ingrediente_id)
            
            nuevo_proveedor_ingrediente = product_prov(
                FK_nit_prov =nuevo_proveedor,
                FK_ID_ing=nuevo_ingrediente,
                precio_prov=nuevo_precio
            )
            nuevo_proveedor_ingrediente.save()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})



def gestion_recetario(request):
    return render(request, 'botones.html')

def directorio_ensalada(request):
    ingredientes = ingrediente.objects.all()
    receta= recetas.objects.all()
    ensalada= ensaladas.objects.all()
    return render(request, 'EnsaladasPrep.html', {'ingredientes': ingredientes, 'receta':receta,  'ensalada': ensalada})

def eliminar_ensalada_ing(request):
    if request.method == 'GET':
        id_producto = request.GET.get('idProducto')
        try:
            Ingrediente = recetas.objects.get(id=id_producto)
            Ingrediente.delete()
            return HttpResponse(json.dumps({'success': True}), content_type='application/json')
        except ingrediente.DoesNotExist:
            return HttpResponse(json.dumps({'success': False, 'message': 'No existe.'}), content_type='application/json')
        except Exception as e:
            return HttpResponse(json.dumps({'success': False, 'message': str(e)}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'success': False, 'message': 'Método no permitido'}), content_type='application/json')

def agregar_ensalada_ing(request):
    if request.method == 'GET':
        nueva_ensalada = request.GET.get('ensaladanueva')
        nuevo_ingrediente = request.GET.get('ingredientenuevo')
        
        try:
            nuevo_proveedor = ensaladas.objects.get(ID_ensalada=nueva_ensalada)
            nuevo_ingrediente = ingrediente.objects.get(ID_ing=nuevo_ingrediente)
            
            nuevo_proveedor_ingrediente = recetas(
                FK_ID_ensalada =nuevo_proveedor,
                FK_ID_ing=nuevo_ingrediente,
            )
            nuevo_proveedor_ingrediente.save()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})

def recetario(request):
    ingredientes = ingrediente.objects.all()
    receta= recetas.objects.all()
    ensalada= ensaladas.objects.all()
    return render(request, 'recetario.html', {'ingredientes': ingredientes, 'receta':receta,  'ensalada': ensalada})

def eliminar_recetario(request):
    if request.method == 'GET':
        id_producto = request.GET.get('idProducto')
        try:
            elimina = ensaladas.objects.get(ID_ensalada=id_producto)
            elimina.delete()
            return HttpResponse(json.dumps({'success': True}), content_type='application/json')
        except ingrediente.DoesNotExist:
            return HttpResponse(json.dumps({'success': False, 'message': 'No existe.'}), content_type='application/json')
        except Exception as e:
            return HttpResponse(json.dumps({'success': False, 'message': str(e)}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'success': False, 'message': 'Método no permitido'}), content_type='application/json')

from django.http import JsonResponse

def editar_recetario(request):
    if request.method == 'GET':
        id_ensa = request.GET.get('idProducto')
        foto = request.GET.get('FK_nit_prov')
        nombre = request.GET.get('FK_ID_ing')
        cate = request.GET.get('precio_prov')
        
        try:
            ENSALADA_editado = ensaladas.objects.get(ID_ensalada=id_ensa)
            if cate:
                ENSALADA_editado.categoria = cate
            if foto:
                ENSALADA_editado.image = foto
            
            if nombre:
                ENSALADA_editado.nom_ensalada = nombre
            
            ENSALADA_editado.save()

            return JsonResponse({'success': True})
        except ingrediente.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Error al editar: ensalada no encontrado.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})

def agregar_recetario(request):
    if request.method == 'GET':
        recetaID = request.GET.get('recetaId')
        imagen = request.GET.get('proveedor')
        nom_ensa = request.GET.get('ingrediente')
        categoriap = request.GET.get('precio')  # Corregido

        try:  
            nuevo_proveedor_ingrediente = ensaladas(
                ID_ensalada=recetaID,
                nom_ensalada=nom_ensa,
                image=imagen,
                categoria=categoriap  # Asignar categoriap a la categoría de la ensalada
            )
            nuevo_proveedor_ingrediente.save()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})


def mostrar_reclamo(request):
    reclamos_usuario = reclamo.objects.all()

    return render(request, 'mostrar_reclamo_admin.html', {'reclamos_usuario': reclamos_usuario})
                                                  
def borrar_reclamo(request, reclamo_id):
    reclamo_obj = get_object_or_404(reclamo, pk=reclamo_id)
    if request.method == 'POST':
        reclamo_obj.delete()
        return redirect('admin:mostrar_reclamo_admin.html')
    return render(request, 'mostrar_reclamo_admin.html', {'reclamo_borrar': reclamo_obj})

    