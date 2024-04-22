from django.urls import path

from . import views

app_name = "app_produccion"

urlpatterns = [
    path('inventario', views.inventario, name='inventario'),
    path('Editarproducto', views.Editarproducto, name='Editarproducto'),
    path('ingenieria', views.ingenieria, name='ingenieria'),
    path('EditarFormula', views.EditarFormula, name='EditarFormula'),
    path('procesos', views.procesos, name='procesos'),
    path('EditarProceso', views.EditarProceso, name='EditarProceso'),
    path('detalleprocesos', views.detalleprocesos, name='detalleprocesos'),
    path('produccion', views.produccion, name='produccion'),
    path('logistica', views.logistica, name='logistica'),
    path('mantenimiento', views.mantenimiento, name='mantenimiento'),
    path('seguridad', views.seguridad, name='seguridad'),
]