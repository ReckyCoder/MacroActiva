from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.index, name='menupostulaciones'),
    path('menu/gestionarPostulaciones/', views.gestionarPostulaciones, name='rhGestionarPostulaciones')
]