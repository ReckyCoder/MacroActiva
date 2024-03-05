from django.urls import path

from . import views

app_name = "app_produccion"

urlpatterns = [
    path('inventario', views.inventario, name='inventario'),
    path('ingenieria', views.ingenieria, name='ingenieria'),
    path('procesos', views.procesos, name='procesos'),
    path('produccion', views.produccion, name='produccion'),
    path('logistica', views.logistica, name='logistica'),
    path('mantenimiento', views.mantenimiento, name='mantenimiento'),
    path('seguridad', views.seguridad, name='seguridad'),
]