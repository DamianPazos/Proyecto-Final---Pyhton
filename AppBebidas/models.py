from django.db import models

# Create your models here.

class Cerveza(models.Model):
    marca=models.CharField(max_length=15)
    tipo=models.CharField(max_length=15)
    capacidad=models.IntegerField()
    
    def __str__(self):
        return f'{self.marca} - Tipo {self.tipo} de {self.capacidad} cm3'
    
class vino(models.Model):
    marca=models.CharField(max_length=15)
    tipo=models.CharField(max_length=15)
    capacidad=models.DecimalField(decimal_places=2,max_digits=4)
    
class gaseosa(models.Model):
    marca=models.CharField(max_length=15)
    tipo=models.CharField(max_length=15)
    capacidad=models.DecimalField(decimal_places=2,max_digits=4)    
    light=models.BooleanField()
