from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class cliente (models.Model):
    
    ced_client = models.AutoField(primary_key=True)
    nom_client = models.CharField(max_length=20)
    correo_client = models.CharField(max_length=30)
    contraseña_client = models.CharField(max_length=128)
    tel_client = models.CharField(max_length=10)
    direc_client = models.CharField(max_length=30)
    ciudad_client = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        # Verificar si la contraseña ya está hasheada
        if not self.contrasena_emp.startswith('pbkdf2_sha256'):
            # Hashear la contraseña antes de guardarla en la base de datos
            self.contrasena_emp = make_password(self.contrasena_emp)
        super().save(*args, **kwargs)

class putuacion (models.Model):
    num_estrellas = models.IntegerField(max_length=1)
    comentario = models.CharField(max_length=50)
    FK_ced_client = models.ForeignKey(cliente, on_delete=models.CASCADE)

class reclamo (models.Model):
    des_recla = models.CharField(max_length=50)
    fecha_reclamo = models.DateField
    FK_ced_client = models.ForeignKey(cliente, on_delete=models.CASCADE)
    #falta imagen reclamo
   

