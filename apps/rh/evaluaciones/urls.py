from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.index, name='menuevaluaciones'),
    path('menu/gestionarEvaluaciones/', views.gestionarEvaluaciones, name='rhGestionarEvaluaciones'),
]