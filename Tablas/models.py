from django.db import models

from django.contrib.auth.models import User

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

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, default="1")

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
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
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
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    total = models.PositiveIntegerField()

    def __str__(self):
        return f"Compra #{self.id} - {self.user}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto} (Compra #{self.venta.id})"
