from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string


# Create your views here.
def index(request):

    context = {
        'mainModuleName': 'recursos_humanos',
        'modulos': [
            {'parentModuleName': 'evaluaciones'},
            {'childModuleName': 'gestor_evaluaciones'}  # default
        ],
        'defaultUrl': 'menuevaluaciones',
        'defaultChildUrl': 'rhGestionarEvaluaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/rh/evaluaciones.html', context=context)


def gestionarEvaluaciones(request):
    
    if request.method == 'GET':

        if request.GET.get('element_id'):

            tipoSolicitud = (request.GET.get('element_id'))

            if (tipoSolicitud[:3] == 'R02'):

                tipoSolicitud = tipoSolicitud[3:-4]

                tipoSolicitudContext = ''.join(
                    ['_' + char.lower() if char.isupper() else char for char in tipoSolicitud]).lstrip('_')

                context = {
                    'meta': {
                        'mainModuleName': 'recursos_humanos',
                        'modulos': [
                            {'parentModuleName': 'evaluaciones'},
                            {'childModuleName': 'gestor_evaluaciones'},  # default
                            {'subChildModuleName': tipoSolicitudContext},
                        ],
                        'defaultUrl': 'menuevaluaciones',
                        'defaultChildUrl': 'rhGestionarEvaluaciones',
                        'defaultSubChildUrl': ''
                    }
                }

                if (tipoSolicitud == 'AgregarEmpleado'):

                    context['meta'].update(
                        {'defaultSubChildUrl': 'rhAgregarEmpleado'})

                    rendered = render_to_string(
                        'pages/rh/empleados/crud-empleados/agregar.html')

                    content = {
                        'HTMLData': rendered,
                        'MetaData': context
                    }

                    return JsonResponse(content)

                elif (tipoSolicitud == 'ModificarEmpleado'):

                    context['meta'].update(
                        {'defaultSubChildUrl': 'rhModificarEmpleado'})

                    rendered = render_to_string(
                        'pages/rh/empleados/crud-empleados/modificar.html')

                    content = {
                        'HTMLData': rendered,
                        'MetaData': context
                    }

                    return JsonResponse(content)

                elif (tipoSolicitud == 'EliminarEmpleado'):

                    context['meta'].update(
                        {'defaultSubChildUrl': 'rhEliminarEmpleado'})

                    rendered = render_to_string(
                        'pages/rh/empleados/crud-empleados/eliminar.html')

                    content = {
                        'HTMLData': rendered,
                        'MetaData': context
                    }

                    return JsonResponse(content)

            context = {
                'mainModuleName': 'recursos_humanos',
                'modulos': [
                    {'parentModuleName': 'evaluaciones'},
                    {'childModuleName': 'gestionar_evaluaciones'}
                ],
                'defaultUrl': 'menuevaluaciones',
                'defaultChildUrl': 'rhGestionarEvaluaciones'
            }

            rendered = render_to_string(
                'pages/rh/evaluaciones/gestionar-evaluaciones.html')

            content = {'HTMLData': rendered,
                       'MetaData': context
                       }

            return JsonResponse(content)
    else:

        context = {
            'mainModuleName': 'recursos_humanos',
            'modulos': [
                {'parentModuleName': 'evaluaciones'},
                {'childModuleName': 'gestionar_evaluaciones'}
            ],
            'defaultUrl': 'menuevaluaciones',
            'defaultChildUrl': 'rhGestionarEvaluaciones'
        }

        content = {'HTMLData': '',
                   'MetaData': context
                   }

        return JsonResponse(content)

    context = {
        'meta': {
            'mainModuleName': 'recursos_humanos',
            'modulos': [
                {'parentModuleName': 'evaluaciones'},
                {'childModuleName': 'gestionar_evaluaciones'},
            ],
            'defaultUrl': 'menuevaluaciones',
            'defaultChildUrl': 'rhGestionarEvaluaciones',
        }
    }

    rendered = render_to_string(
        'pages/rh/evaluaciones/gestionar-evaluaciones.html')

    content = {
        'HTMLData': rendered,
        'MetaData': context
    }

    return JsonResponse(content)