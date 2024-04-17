from django.db import models

class ingrediente (models.Model):
    ID_ing = models.IntegerField(primary_key=True)
    nom_ing=models.CharField(max_length=20)
    cant_gramos= models.FloatField()
    cant_min= models.FloatField()
    precio_min= models.FloatField()
    
class ensaladas (models.Model):
     ID_ensalada = models.IntegerField(primary_key=True)
     nom_ensalada = models.CharField(max_length=20)
     
class recetas (models.Model):
    FK_ID_ing = models.ForeignKey(ingrediente, on_delete=models.CASCADE)
    FK_ID_ensalada = models.ForeignKey(ensaladas, on_delete=models.CASCADE)
     
class proveedor (models.Model):
    nit = models.IntegerField(primary_key=True)
    nom_prov = models.CharField(max_length=20)
    correo_prov = models.CharField(max_length=30)
    tel_prov = models.CharField(max_length=10)
    ciudad_prov= models.CharField(max_length=20)
    desc_prov= models.CharField(max_length=50)
    
class product_prov (models.Model):
    FK_nit_prov = models.ForeignKey(proveedor, on_delete=models.CASCADE)
    FK_ID_ing = models.ForeignKey(ingrediente, on_delete=models.CASCADE)
    precio_prov=models.FloatField()
    
    
    
    
# Create your models here.
