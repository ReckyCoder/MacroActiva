from django.urls import path

from . import views

app_name = "app_crmventas"

urlpatterns = [
    #Clientes Ventas
    path('zona', views.zona, name='zona'),
    path('campaña', views.campaña, name='campaña'),
    path('calendariocampaña', views.calendariocampaña, name='calendariocampaña'),
    path('clientes_leads', views.clientes_leads, name='clientes_leads'),
    path('cotizaciones', views.cotizaciones, name='cotizaciones'),
    path('ventas', views.ventas, name='ventas'),
    path('contratoscv', views.contratoscv, name='contratoscv'),
    path('postventa', views.postventa, name='postventa'),
    path('reembolso', views.reembolso, name='reembolso'),
    path('soporte', views.soporte, name='soporte'),
]