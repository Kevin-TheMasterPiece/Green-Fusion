from django.db import models
from django.contrib.auth.hashers import make_password

class rol(models.Model):
    nom_Rol = models.CharField(max_length=20)
    
class empleado(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nom_emp = models.CharField(max_length=20)
    correo_emp = models.CharField(max_length=30)
    contrasena_emp = models.CharField(max_length=128)  
    tel_emp = models.CharField(max_length=10)
    direc_emp = models.CharField(max_length=30)
    ciudad_emp = models.CharField(max_length=20)
    foto_emp = models.ImageField(upload_to='empleado/')
    ID_Rol = models.ForeignKey(rol, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Verificar si la contraseña ya está hasheada
        if not self.contrasena_emp.startswith('pbkdf2_sha256'):
            # Hashear la contraseña antes de guardarla en la base de datos
            self.contrasena_emp = make_password(self.contrasena_emp)
        super().save(*args, **kwargs)