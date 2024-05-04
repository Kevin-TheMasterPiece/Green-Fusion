from django.contrib import admin
from .models import ingrediente, ensaladas, recetas
# Register your models here.

@admin.register(ingrediente)
class IngredienteAdmin (admin.ModelAdmin):
 list_display = ['ID_ing', 'nom_ing', 'cant_gramos', 'cant_min', 'precio_min', 'image']
 list_editable = ['nom_ing', 'cant_gramos', 'cant_min', 'precio_min', 'image']
 list_filter = ['activo']


@admin.register(ensaladas)
class EnsaladasAdmin (admin.ModelAdmin):
 list_display= ['ID_ensalada', 'nom_ensalada', 'activo', 'image', 'categoria']
 list_editable = ['nom_ensalada', 'activo', 'image', 'categoria']
 list_filter = ['activo']

 @admin.register(recetas)
 class RecetasAdmin (admin.ModelAdmin):
  list_display = ['FK_ID_ensalada', 'FK_ID_ing']
  list_editable = ['FK_ID_ing']
  list_filter = ['FK_ID_ensalada']
  


