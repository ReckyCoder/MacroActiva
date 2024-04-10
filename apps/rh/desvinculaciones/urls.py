from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.index, name='menudesvinculaciones'),
    path('menu/gestionarDesvinculaciones/', views.gestionarDesvinculaciones, name='rhGestionarDesvinculaciones')
]