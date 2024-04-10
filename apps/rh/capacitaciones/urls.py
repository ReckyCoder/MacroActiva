from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.index, name='menucapacitaciones'),
    path('menu/gestionarCapacitaciones/', views.gestionarCapacitaciones, name='rhGestionarCapacitaciones'),
]