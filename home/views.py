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

def inventario(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Producción"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}
    
    return render(request, 'pages/Produccion/inventario.html', context=context)

def ingenieria(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Producción"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}
    
    return render(request, 'pages/Produccion/ingenieria.html', context=context)

def procesos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Producción"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}
    
    return render(request, 'pages/Produccion/procesos.html', context=context)

def produccion(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Producción"
    nombre_vista = "Producción"
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}
    
    return render(request, 'pages/Produccion/produccion.html', context=context)

def logistica(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Producción"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}
    
    return render(request, 'pages/Produccion/logistica.html', context=context)

def mantenimiento(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Producción"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}
    
    return render(request, 'pages/Produccion/mantenimiento.html', context=context)

def seguridad(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Producción"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}
    
    return render(request, 'pages/Produccion/seguridad.html', context=context)
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
