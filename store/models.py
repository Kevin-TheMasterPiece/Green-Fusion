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
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

class factura_ensalda (models.Model):
    FK_factura = models.ForeignKey(factura, on_delete=models.CASCADE)
    FK_ensalada = models.ForeignKey(ensaladas, on_delete=models.CASCADE)
    tamaño = models.CharField(max_length=10)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

