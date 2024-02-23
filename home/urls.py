from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('zona', views.zona, name='zona'),
    path('campaña', views.campaña, name='campaña'),
]
