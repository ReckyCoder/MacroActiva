from django.shortcuts import render

# Create your views here.

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

def gestionproductos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administración/gestionproductos.html', context=context)

def contratos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administración/contratos.html', context=context)

def contrato(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administración/contrato.html', context=context)

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

def licitaciones(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administración/licitaciones.html', context=context)

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