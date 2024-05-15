from django.contrib import admin
from .models import factura, factura_ensalda

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = factura_ensalda
    raw_id_fields = ['FK_ensalada']


@admin.register(factura)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'FK_ced_client',
                    'direccion', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]