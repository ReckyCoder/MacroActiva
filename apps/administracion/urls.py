from django.urls import path

from . import views

app_name = "app_administracion"

urlpatterns = [
    #----------------------------- Administracion ---------------------------
    path('departamentos', views.departamentos, name='departamentos'),
    path('departamento', views.vistadepartamento, name='departamento'),
    path('productos', views.productos, name='productos'),
    path('ordenesproductos', views.ordenesproductos, name='ordenesproductos'),
    path('contratos', views.contratos, name='contratos'),
    path('certificaciones', views.certificaciones, name='certificaciones'),
    path('proveedores', views.proveedores, name='proveedores'),
    path('proyectos', views.proyectos, name='proyectos'),
    path('kpi', views.kpi, name='kpi')


]