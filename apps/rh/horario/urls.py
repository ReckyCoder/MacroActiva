from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.index, name='menuhorario'),
    path('menu/gestionarHorario/', views.gestionarHorario, name='rhGestionarHorario'),
]