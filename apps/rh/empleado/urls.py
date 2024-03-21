from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.index, name='menuempleado'),
    path('menu/gestionarEmpleados/', views.gestionarEmpleados, name='rhGestionarEmpleados'),
    path('menu/agregarEmpleadoView/', views.gestionarEmpleados, name='rhAgregarEmpleado'),
    path('menu/modificarEmpleadoView/', views.gestionarEmpleados, name='rhModificarEmpleado'),
    path('menu/eliminarEmpleadoView/', views.gestionarEmpleados, name='rhEliminarEmpleado'),
]