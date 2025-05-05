from django.db import models
from django.utils import timezone
# -----------------------
# MODELOS BÁSICOS
# -----------------------

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

# -----------------------
# MODELO DE USUARIOS
# -----------------------

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    username = models.CharField(unique=True, max_length=20)
    contrasena = models.CharField(max_length=25)
    celular = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, default=1)
    foto = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    direccion = models.CharField(max_length=255)
    codigopostal = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# -----------------------
# MODELOS DE PRODUCTOS
# -----------------------

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=150)
    precio = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    foto = models.ImageField(upload_to='fotos_productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre_producto

# -----------------------
# CARRITO DE COMPRAS
# -----------------------

class Carrito(models.Model):
    fecha_creacion = models.DateTimeField(default=timezone.now)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    @property
    def total(self):
        return self.cantidad * self.producto.precio

    def __str__(self):
        return f"Carrito de {self.cliente} - {self.producto} x {self.cantidad}"

# -----------------------
# VENTAS Y DETALLE DE VENTA
# -----------------------

class Venta(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    total = models.PositiveIntegerField()

    def __str__(self):
        return f"Compra #{self.id} - {self.cliente}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto} (Compra #{self.venta.id})"
