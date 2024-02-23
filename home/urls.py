from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #Clientes Ventas
    path('zona', views.zona, name='zona'),
    path('campaña', views.campaña, name='campaña'),
    #Administracion
    path('departamentos', views.departamentos, name='departamentos'),
    path('productos', views.productos, name='productos'),
    path('contratos', views.contratos, name='contratos'),
    path('certificaciones', views.certificaciones, name='certificaciones'),
    path('proveedores', views.proveedores, name='proveedores'),
    path('proyectos', views.proyectos, name='proyectos'),
    path('kpi', views.kpi, name='kpi')
]
