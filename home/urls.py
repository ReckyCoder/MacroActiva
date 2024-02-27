from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('inventario', views.inventario, name='inventario'),
    path('ingenieria', views.ingenieria, name='ingenieria'),
    path('procesos', views.procesos, name='procesos'),
    path('produccion', views.produccion, name='produccion'),
    path('logistica', views.logistica, name='logistica'),
    path('mantenimiento', views.mantenimiento, name='mantenimiento'),
    path('seguridad', views.seguridad, name='seguridad'),
    path('departamentos', views.departamentos, name='departamentos'),
    path('departamento', views.vistadepartamento, name='departamento'),
    path('productos', views.productos, name='productos'),
    path('contratos', views.contratos, name='contratos'),
    path('certificaciones', views.certificaciones, name='certificaciones'),
    path('proveedores', views.proveedores, name='proveedores'),
    path('proyectos', views.proyectos, name='proyectos'),
    path('kpi', views.kpi, name='kpi')
]
