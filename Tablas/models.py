from django.db import models

# Categorías primero
class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre}"

class CategoriaJuego(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre}"

class Rol(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.nombre}"
# Luego los modelos que las usan
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    username = models.CharField(unique=True, max_length=20)
    contrasena = models.CharField(max_length=25)
    celular = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE,default=1)
    foto = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    direccion = models.CharField(max_length=255)
    codigopostal = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=150)
    precio = models.PositiveIntegerField()
    categoria_productos = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    stock = models.IntegerField()
    foto = models.ImageField(upload_to='fotos_productos/', null=True, blank=True)
    def __str__(self):
        return f"{self.nombre_producto}"

class Juegos(models.Model):
    nombre_juego = models.CharField(max_length=150)
    precio = models.PositiveIntegerField()
    categoria_juegos = models.ForeignKey(CategoriaJuego, on_delete=models.CASCADE)
    ventas= models.PositiveIntegerField() #como le hacesAAAAAAAAAAAAAAAAAA
    foto = models.ImageField(upload_to='fotos_juegos/', null=True, blank=True)
    def __str__(self):
        return f"{self.nombre_juego}"

class Licencias(models.Model):
    nombre_licencia = models.CharField(max_length=150)
    precio = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=500)
    ventas= models.PositiveIntegerField() #como le hacesAAAAAAAAAAAAAAAAAA
    foto = models.ImageField(upload_to='fotos_licencias/', null=True, blank=True)
    def __str__(self):
        return f"{self.nombre_licencia}"
