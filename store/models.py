from django.db import models
from django.contrib.auth.hashers import make_password
from administrador.models import ensaladas
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class reclamo (models.Model):
    des_recla = models.CharField(max_length=50)
    fecha_reclamo = models.DateField(default=timezone.now)
    FK_ced_client = models.ForeignKey(User, on_delete=models.CASCADE)
    foto_reclamo = models.ImageField(upload_to='reclamos/')
   
class factura (models.Model):
    fecha_factura = models.DateField
    FK_ced_client = models.ForeignKey(User, on_delete=models.CASCADE)
    nom_client = models.CharField(max_length=30, default='')
    apell_client = models.CharField(max_length=30, default='')
    direccion = models.CharField(max_length=250, default='')
    city = models.CharField(max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    preparada= models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Factura {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class factura_ensalda (models.Model):
    FK_factura = models.ForeignKey(factura, related_name='items', on_delete=models.CASCADE)
    FK_ensalada = models.ForeignKey(ensaladas, related_name='order_items', on_delete=models.CASCADE)
    tamaño = models.CharField(max_length=10)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.subtotal * self.quantity

