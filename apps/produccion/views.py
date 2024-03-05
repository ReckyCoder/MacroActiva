from django.shortcuts import render

# Create your views here.
def inventario(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Producción"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}
    
    return render(request, 'pages/Produccion/inventario.html', context=context)

def ingenieria(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Producción"
    nombre_vista = "Ingeniería"
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