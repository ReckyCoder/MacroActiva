from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #Clientes Ventas
    path('', include('apps.crmventas.urls')),
    #Administracion
    path('', include('apps.finanzas.urls')),
    path('departamentos', views.departamentos, name='departamentos'),
    path('departamento', views.vistadepartamento, name='departamento'),
    path('productos', views.productos, name='productos'),
    path('contratos', views.contratos, name='contratos'),
    path('certificaciones', views.certificaciones, name='certificaciones'),
    path('proveedores', views.proveedores, name='proveedores'),
    path('proyectos', views.proyectos, name='proyectos'),
    path('kpi', views.kpi, name='kpi')
]
