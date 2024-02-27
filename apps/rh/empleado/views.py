from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps

# Create your views here.

def index(request):

    context = {
        'mainModuleName': 'recursos_humanos',
        'modulos': [
            {'parentModuleName': 'empleados'},
            #{'childModuleName': ''} en caso de que existan mas paginaciones
        ],
        'defaultUrl':'menuempleado',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme 
    return render(request, 'pages/rh/empleados.html', context=context)