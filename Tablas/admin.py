from django.contrib import admin
from django.contrib.auth.models import User
from .models import Producto, Categoria, Carrito, Rol,Venta, DetalleVenta, PerfilUsuario
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
  list_display=("nombre_producto", "precio", "stock")

admin.site.register(PerfilUsuario)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
admin.site.register(Carrito)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Rol)
