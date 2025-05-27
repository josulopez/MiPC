from django.http import HttpResponse
from django.template import loader
from .models import Producto, Carrito, Venta, DetalleVenta
from .forms import CustomAuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# def nombre de la pagina
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Reemplaza 'home' con el nombre de tu vista principal
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})
def info(request):
  template = loader.get_template('info.html')
  return HttpResponse(template.render({}, request))

def juegos(request):
  juegos = Producto.objects.filter(categoria__nombre__icontains='juegos')
  context = {
    "juegos" : juegos
  }
  template = loader.get_template('juegos.html')
  return HttpResponse(template.render(context,request))

def componentes(request):
  componentes = Producto.objects.filter(categoria__nombre__icontains='componentes')
  context = {
    "componentes" : componentes
  }
  template = loader.get_template('componentes.html')
  return HttpResponse(template.render(context,request))

def licencias(request):
  licencias = Producto.objects.filter(categoria__nombre__icontains='licencias')
  context = {
    "licencias" : licencias
  }
  template = loader.get_template('licencias.html')
  return HttpResponse(template.render(context,request))

def Main(request):
  videojuegos = Producto.objects.filter(categoria__nombre__icontains='juegos')
  componentes = Producto.objects.filter(categoria__nombre__icontains='componentes')
  licencias = Producto.objects.filter(categoria__nombre__icontains='licencias')
  context = {
      "videojuegos": videojuegos,
      "componentes": componentes,
      "licencias": licencias,
  }
  template = loader.get_template('main.html')
  return HttpResponse(template.render(context, request))

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item, creado = Carrito.objects.get_or_create(
        cliente=request.user,
        producto=producto
    )
    if not creado:
        carrito_item.cantidad += 1
        carrito_item.save()
    return redirect('ver_carrito')

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(Carrito, id=item_id, cliente=request.user)
    item.delete()
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito_items = Carrito.objects.filter(cliente=request.user)
    total_general = sum(item.total for item in carrito_items)

    return render(request, 'carrito.html', {
        'carrito_items': carrito_items,
        'total_general': total_general,
    })

@login_required
def pagar_carrito(request):
    carrito_items = Carrito.objects.filter(cliente=request.user)
    if not carrito_items.exists():
        return redirect('ver_carrito')  # Or handle empty cart

    # Calculate total
    total = sum(item.total for item in carrito_items)

    # Create Venta
    venta = Venta.objects.create(
        cliente=request.user,
        total=total
    )

    # Create DetalleVenta entries
    for item in carrito_items:
        DetalleVenta.objects.create(
            venta=venta,
            producto=item.producto,
            cantidad=item.cantidad,
            subtotal=item.total
        )

    # Clear the cart
    carrito_items.delete()

    return redirect('gracias')

def gracias(request):
    return render(request, 'gracias.html')
