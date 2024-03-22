from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

def index(request):

    context = {
        'mainModuleName': 'recursos_humanos',
        'modulos': [
            {'parentModuleName': 'postulaciones'},
            {'childModuleName': 'gestor_contratos'}  # default
        ],
        'defaultUrl': 'menupostulaciones',
        'defaultChildUrl': 'rhGestionarContratos',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/rh/postulaciones.html', context=context)