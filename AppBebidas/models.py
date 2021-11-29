from django.db import models

# Create your models here.

class cerveza(models.Model):
    marca=models.CharField(max_length=15)
    tipo=models.CharField(max_length=15)
    capacidad=models.DecimalField(decimal_places=2,max_digits=4)
    
class vino(models.Model):
    marca=models.CharField(max_length=15)
    tipo=models.CharField(max_length=15)
    capacidad=models.DecimalField(decimal_places=2,max_digits=4)
    
class gaseosa(models.Model):
    marca=models.CharField(max_length=15)
    tipo=models.CharField(max_length=15)
    capacidad=models.DecimalField(decimal_places=2,max_digits=4)    
    light=models.BooleanField()
