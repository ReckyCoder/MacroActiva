from django.urls import path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('menu/', views.index, name='menuremuneraciones'),
    path('menu/fichaEmpleados/', views.fichasEmpleados, name='rhFichaEmpleados'),
    path('menu/PersonalView/', views.fichasEmpleados, name='rhFichaPersonalView'),
    path('menu/LaboralView/', views.fichasEmpleados, name='rhFichaLaboralView'),
    path('menu/modeloCalculo/', views.modeloCalculo, name='rhModeloCalculo'),
]

handler404 = ''