from django.shortcuts import render

# Create your views here.

def departamentos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/departamentos.html', context=context)

def vistadepartamento(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/Vista-Departamento.html', context=context)

def productos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/productos.html', context=context)

def gestionproductos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/gestionproductos.html', context=context)

def contratos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/contratos.html', context=context)

def contrato(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/contrato.html', context=context)

def certificaciones(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/certificaciones.html', context=context)

def proveedores(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/proveedores.html', context=context)

def licitaciones(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/licitaciones.html', context=context)

def proyectos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/proyectos.html', context=context)

def kpi(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/kpi.html', context=context)