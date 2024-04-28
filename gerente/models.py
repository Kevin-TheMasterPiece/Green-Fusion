from django.db import models

class Rol(models.Model):
    nom_Rol = models.CharField(max_length=20)
class empleado(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nom_emp = models.CharField(max_length=20)
    correo_emp = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=128, default=' ')
    tel_emp = models.CharField(max_length=10)
    direc_emp = models.CharField(max_length=30)
    ciudad_emp = models.CharField(max_length=20)
    foto_emp = models.ImageField(upload_to='empleado/')
    FK_ID_Rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        super(empleado, self).save(*args, **kwargs)