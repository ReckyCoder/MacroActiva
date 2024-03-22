from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.index, name='menucontrataciones'),
    path('menu/gestionarContratos/', views.gestionarContratos, name='rhGestionarContratos'),
]