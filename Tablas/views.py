from django.http import HttpResponse
from django.template import loader
from .models import Usuario
from .models import Producto
# def nombre de la pagina
  
def clientes(request):
  misclientes = Usuario.objects.all().values()
  template = loader.get_template('clientes.html')
  context = {
    'misclientes': misclientes,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  micliente = Usuario.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'micliente': micliente,
  }
  return HttpResponse(template.render(context, request))

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

def testing(request):
  clientes = Usuario.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'clientes': clientes,   
  }
  return HttpResponse(template.render(context, request))