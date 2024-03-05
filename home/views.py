from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    context = {
        'mainModuleName': 'inicio',
        'defaultUrl':'dashboard',
    }

    # Page from the theme 
    return render(request, 'pages/dashboard.html', context=context)

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


def departamentos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administración/departamentos.html', context=context)

def vistadepartamento(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administración/Vista-Departamento.html', context=context)

def productos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administración/productos.html', context=context)

def contratos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administración/contratos.html', context=context)

def certificaciones(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administración/certificaciones.html', context=context)

def proveedores(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administración/proveedores.html', context=context)

def proyectos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administración/proyectos.html', context=context)

def kpi(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administración/kpi.html', context=context)
