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
    context = {
        'mainModuleName': 'Clientes Ventas',
        'modulos': [
            {'parentModuleName': 'Cotizaciones'},
            #{'childModuleName': 'Editar Proceso'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/CLIENTES-VENTAS/cotizaciones.html', context=context)

def cotizacionCrear(request):
    context = {
        'mainModuleName': 'Clientes Ventas',
        'modulos': [
            {'parentModuleName': 'Cotizaciones'},
            {'childModuleName': 'Crear Cotización'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/CLIENTES-VENTAS/cotizacionesCrear.html', context=context)


def ventas(request):
    context = {
        'mainModuleName': 'Clientes Ventas',
        'modulos': [
            {'parentModuleName': 'Ventas'},
            #{'childModuleName': 'Editar Proceso'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
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

def reembolso(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/postventa/reembolso.html', context=context)

def soporte(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/postventa/soporte.html', context=context)