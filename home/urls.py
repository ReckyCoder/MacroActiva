from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #Clientes Ventas
    path('', include('apps.crmventas.urls')),
    #Administracion
    path('', include('apps.produccion.urls')),
    path('', include('apps.finanzas.urls')),
    path('', include('apps.administracion.urls')),
]
