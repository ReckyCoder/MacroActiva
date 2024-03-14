from django.shortcuts import render

from django.views.generic import ListView, TemplateView, CreateView
# Create your views here.
def zona(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}
   
    return render(request, 'pages/CLIENTES-VENTAS/zona.html', context=context)

def campaña(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/campaña.html', context=context)

def calendariocampaña(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/Campañaitems/calendarioact.html', context=context)

def clientes_leads(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/leads-clientes.html', context=context)

def cotizaciones(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/cotizaciones.html', context=context)

def ventas(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/ventas.html', context=context)

def contratoscv(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/contratoscv.html', context=context)

def postventa(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/postventa.html', context=context)