from django.db import models
from django.urls import reverse

class ingrediente (models.Model):
    ID_ing = models.IntegerField(primary_key=True)
    nom_ing = models.CharField(max_length=20)
    cant_gramos= models.FloatField()
    cant_min = models.FloatField(verbose_name='Cantidad minima (gramos)')
    precio_min = models.FloatField()
    activo = models.BooleanField(default=True)
    image = models.CharField(max_length=200, default='')

    def __str__(self) -> str:
        return self.nom_ing
    
class ensaladas (models.Model):
     ID_ensalada = models.IntegerField(primary_key=True)
     nom_ensalada = models.CharField(max_length=20)
     activo = models.BooleanField(default=True) #para desactuvar una ensalda y borrarla de la base de datos
     image = models.CharField(max_length=200, default='')
     categoria = models.CharField(max_length=50, default='')

     def get_absolute_url(self):
        return reverse('store:detalles_ensalada',
                       args=[self.ID_ensalada, self.nom_ensalada])

     class Meta:
        verbose_name = 'Ensadala'
        verbose_name_plural = 'Ensadalas'
     
     def __str__(self) -> str:
         return  self.nom_ensalada

class recetas (models.Model):
    FK_ID_ing = models.ForeignKey(ingrediente, on_delete=models.CASCADE, verbose_name='Ingrediente')
    FK_ID_ensalada = models.ForeignKey(ensaladas, on_delete=models.CASCADE, verbose_name='Ensalada')

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
     
class proveedor (models.Model):
    nit = models.IntegerField(primary_key=True)
    nom_prov = models.CharField(max_length=20)
    correo_prov = models.CharField(max_length=30)
    tel_prov = models.CharField(max_length=10)
    ciudad_prov= models.CharField(max_length=20)
    desc_prov= models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nom_prov
    
class product_prov (models.Model):
    FK_nit_prov = models.ForeignKey(proveedor, on_delete=models.CASCADE)
    FK_ID_ing = models.ForeignKey(ingrediente, on_delete=models.CASCADE)
    precio_prov=models.FloatField()
    
    
    
    
# Create your models here.
