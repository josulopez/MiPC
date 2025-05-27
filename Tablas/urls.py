from django.urls import path
from . import views
#path('ruta de la web', view.objeto de views)
urlpatterns = [
    path('', views.Main, name='Main'),
    path('juegos', views.juegos, name='juegos'),
    path('componentes', views.componentes, name='componentes'),
    path('licencias', views.licencias, name='licencias'),
    path('info', views.info, name="info"),
    path('login/', views.login_view, name='login'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('pagar/', views.pagar_carrito, name='pagar'),
    path('gracias/', views.gracias, name='gracias'),
]
