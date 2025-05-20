from django.urls import path
from . import views
#path('ruta de la web', view.objeto de views)
urlpatterns = [
    path('', views.Main, name='Main'),
    path('clienteslista/', views.clientes, name='Clientes'),
    path('clienteslista/details/<int:id>', views.details, name='details'),
    path('test/', views.testing, name="test"),
    path('juegos', views.juegos, name='juegos'),
    path('componentes', views.componentes, name='componentes'),
    path('licencias', views.licencias, name='licencias'),
    
]