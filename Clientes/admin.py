from django.contrib import admin
from .models import Cliente , Producto
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
  list_display=("nombre", "apellido", "celular", "email")

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto)
