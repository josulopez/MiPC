from django.contrib import admin
from .models import Usuario, Producto, Categoria, Carrito, Rol,Venta, DetalleVenta
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
  list_display=("nombre", "apellido", "celular", "email")

admin.site.register(Usuario, ClienteAdmin)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Carrito)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Rol)
