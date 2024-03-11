from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', include('apps.finanzas.urls')),
    path('', include('apps.administracion.urls')),
]
