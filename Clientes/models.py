from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    celular=models.IntegerField()
    email=models.EmailField(max_length=255)
    def __str__(self):
        return f"{self.nombre} {self.apellido}" 
    
class Producto(models.Model):
    nombre_producto=models.CharField(max_length=150)
    precio=models.PositiveIntegerField()
    categoria=models.PositiveIntegerField()
