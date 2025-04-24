
from django.contrib import admin
from .models import Cliente , Producto, CategoriaProducto, CategoriaJuego, Juegos, Licencias
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
  list_display=("nombre", "apellido", "celular", "email")

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto)
admin.site.register(CategoriaProducto)
admin.site.register(CategoriaJuego)
admin.site.register(Juegos)
admin.site.register(Licencias)
