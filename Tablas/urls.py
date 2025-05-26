from django.urls import path
from . import views
#path('ruta de la web', view.objeto de views)
urlpatterns = [
    path('', views.Main, name='Main'),
    path('juegos', views.juegos, name='juegos'),
    path('componentes', views.componentes, name='componentes'),
    path('licencias', views.licencias, name='licencias'),
    path('info', views.info, name="info"),
    
]