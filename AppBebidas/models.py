from django.db import models

# Create your models here.

class Cerveza(models.Model):
    marca=models.CharField(max_length=15)
    tipo=models.CharField(max_length=15)
    capacidad=models.IntegerField()
    
    def __str__(self):
        return f'{self.marca} - Tipo {self.tipo} de {self.capacidad} cm3'
    
class Vino(models.Model):
    marca=models.CharField(max_length=15)
    tipo=models.CharField(max_length=15)
    capacidad=models.IntegerField()
    
    def __str__(self):
        return f'{self.marca} - Tipo {self.tipo} de {self.capacidad} cm3'
    
class Gaseosa(models.Model):
    marca=models.CharField(max_length=15)
    tipo=models.CharField(max_length=15)
    capacidad=models.IntegerField()    
    light=models.BooleanField()

    def __str__(self):
        return f'{self.marca} - Tipo {self.tipo} de {self.capacidad} cm3'