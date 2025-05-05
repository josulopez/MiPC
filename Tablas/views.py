from django.http import HttpResponse
from django.template import loader
from .models import Usuario
# def nombre de la pagina
def clienteslista(request):
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

def Clientes(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def Main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  clientes = Usuario.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'clientes': clientes,   
  }
  return HttpResponse(template.render(context, request))