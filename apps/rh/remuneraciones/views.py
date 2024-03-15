from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.template.loader import render_to_string
# Create your views here.


def index(request):

    context = {
        'mainModuleName': 'recursos_humanos',
        'modulos': [
            {'parentModuleName': 'remuneraciones'},
            {'childModuleName': 'fichas_empleados'}  # default
        ],
        'defaultUrl': 'menuremuneraciones',
        'defaultChildUrl': 'rhFichaEmpleados',
    }

    # Page from the theme
    return render(request, 'pages/rh/remuneraciones.html', context=context)



def fichasEmpleados(request):

    if request.method == 'GET':
        

        if request.GET.get('element_id'):
            
            tipoSolicitud = (request.GET.get('element_id'))
            
            
            if (tipoSolicitud[:3] == 'R01'):
                
                
                context = {
                    'mainModuleName': 'recursos_humanos',
                    'modulos': [
                        {'parentModuleName': 'remuneraciones'},
                        {'childModuleName': 'fichas_empleados'}
                    ],
                    'defaultUrl': 'menuremuneraciones',
                    'defaultChildUrl': 'rhFichaEmpleados'
                }

                rendered = render_to_string(
                    'pages/rh/remuneraciones/ficha-empleados.html')

                content = {'HTMLData': rendered,
                        'MetaData': context
                }
                
                return JsonResponse(content)
                
            elif (tipoSolicitud[:3] == 'R02'):
                
                tipoSolicitud = tipoSolicitud[3:-4]
                

                tipoSolicitudContext = ''.join(
                    ['_' + char.lower() if char.isupper() else char for char in tipoSolicitud]).lstrip('_')

                context = {
                    'meta': {
                        'mainModuleName': 'recursos_humanos',
                        'modulos': [
                            {'parentModuleName': 'remuneraciones'},
                            {'childModuleName': 'fichas_empleados'},
                            {'subChildModuleName': tipoSolicitudContext},
                        ],
                        'defaultUrl': 'menuremuneraciones',
                        'defaultChildUrl': 'rhFichaEmpleados',
                        'defaultSubChildUrl': 'rhFichaPersonalView'
                    },
                }

                if tipoSolicitud == 'FichaPersonal':

                    context.update(user_context)

                    rendered = render_to_string(
                        'pages/rh/remuneraciones/fichas/personal.html')

                    content = {
                        'HTMLData': rendered,
                        'MetaData': context
                    }
                    
                    return JsonResponse(content)

                elif tipoSolicitud == 'FichaLaboral':

                    context.update(user_context)
                    
                    
                    rendered = render_to_string(
                        'pages/rh/remuneraciones/fichas/laboral.html')

                    content = {
                        'HTMLData': rendered,
                        'MetaData': context
                    }

                    return JsonResponse(content)
                
                elif tipoSolicitud == 'FichaPago':

                    context.update(user_context)
                    
                    
                    rendered = render_to_string(
                        'pages/rh/remuneraciones/fichas/pago.html')

                    content = {
                        'HTMLData': rendered,
                        'MetaData': context
                    }

                    return JsonResponse(content)
                
                elif tipoSolicitud == 'FichaPrevision':

                    context.update(user_context)
                    
                    
                    rendered = render_to_string(
                        'pages/rh/remuneraciones/fichas/prevision.html')

                    content = {
                        'HTMLData': rendered,
                        'MetaData': context
                    }

                    return JsonResponse(content)
                
                elif tipoSolicitud == 'FichaCompetencias':

                    context.update(user_context)
                    
                    
                    rendered = render_to_string(
                        'pages/rh/remuneraciones/fichas/competencias.html')

                    content = {
                        'HTMLData': rendered,
                        'MetaData': context
                    }

                    return JsonResponse(content)
                
                elif tipoSolicitud == 'FichaCargas':

                    context.update(user_context)
                    
                    
                    rendered = render_to_string(
                        'pages/rh/remuneraciones/fichas/cargas.html')

                    content = {
                        'HTMLData': rendered,
                        'MetaData': context
                    }

                    return JsonResponse(content)
                
                elif tipoSolicitud == 'FichaDocumentos':

                    context.update(user_context)
                    
                    
                    rendered = render_to_string(
                        'pages/rh/remuneraciones/fichas/documentos.html')

                    content = {
                        'HTMLData': rendered,
                        'MetaData': context
                    }

                    return JsonResponse(content)
                
                elif tipoSolicitud == 'FichaHorario':

                    context.update(user_context)
                    
                    
                    rendered = render_to_string(
                        'pages/rh/remuneraciones/fichas/horario.html')

                    content = {
                        'HTMLData': rendered,
                        'MetaData': context
                    }

                    return JsonResponse(content)
    else:
        
        return JsonResponse(content)


def modeloCalculo(request):

    context = {
        'mainModuleName': 'recursos_humanos',
        'modulos': [
            {'parentModuleName': 'remuneraciones'},
            {'childModuleName': 'modelo_calculo'}
        ],
        'defaultUrl': 'menuremuneraciones',
        'defaultChildUrl': 'rhModeloCalculo'
    }

    content = {'HTMLData': "Modelo calculo",
               'MetaData': context
               }
    return JsonResponse(content)


user_context = {
    'user': {  # Usuario predefinido
        'personal': {
            'nombre': 'Daniela',
            'appaterno': 'Contreras',
            'apmaterno': 'Gonzales',
            'rut': '14852654',
            'dv': '6',
            'direccion': 'Las tranqueras 458',
            'comuna': 'Vitacura',
            'cuidad': 'Santiago',
            'estudios': 'Recursos humanos',
            'celular': '+56978452365',
            'fecnacimiento': '25-08-1984',
            'email': 'da.contre@gmail.com',
            'estado_civil': 'Casada',
            'genero': 'Femenino',
            'nacionalidad': 'Chilena',
        },
        'laboral': {
            'cargo': 'Reclutador',
            'id_cargo': '004',
            'area_negocio': 'Casa matriz',
            'id_area_negocio': '004',
            'centro_costo': 'Administracion',
            'id_centro_costo': '654',
            'fec_ingreso': '01-01-2020',
            'fec_primer_contrato': '01-01-2020',
            'fec_contrato_vigente': '01-03-2024',
            'fec_termino_contrato': '',
            'estado': 'Vigente',
            'tipo_mano_obra': '',
            'id_tipo_mano_obra': '',
            'rol_privado': 'No',
            'fec_inicio_vacaciones': '01-12-2024',
            'anios_otro_empleador' :'0',
            'fec_cert_vaciones_progresivas': '01-01-2020',
            'n_dias_vacaciones': '15',
            'tipo_certificado_rentas': 'Sueldos',
            'id_tipo_certificado_rentas': '671',
        },
        'pago': {
            'tipo_pago': 'deposito',
            'datos_bacarios': {
                'rut': '',
                'email': '',
                'nombre_banco': 'Banco de Chile',
                'id_banco': 'B484123',
                'n_cuenta': '4565646351',
                'tipo_cuenta': 'cuenta corriente',
            },
        },
        'prevision': {
            'afp': {
                'nombre': 'AFP Modelo',
                'id_afp': '46542',
                'porc_cotizacion': '10',
                'cotizacion_adicional': {
                    'porc_cotizacion_adicional': '2.45',
                    'tipo_monto_cotizacion_adicional': 'pesos',
                    'monto_cotizacion_adicional': '12758',
                },
            },
            'isapre': {
                'nombre': 'Banmedica',
                'id_isapre': '16521',
                'porc_cotizacion': '11',
                'ley_18566': {
                    'porc_cotizacion': '3.54',
                    'tipo_monto_cotizacion': 'pesos',
                    'monto_contizacion': '8462',
                }
            },
            'caja_compensacion': {
                'nombre': 'Caja de compensacion Los Andes',
                'id_caja_compensacion': '4984132',
            },
            'APVC': {},
        },
        'competencias': {
            1: {
                'Nombre':'Responsabilidad',
                'Descripcion':'Preimiado/a por cumplimiento de reglamentos y tareas',
                'Valor':'20',
                'Fecha vencimiento':'01-01-2024',
                'Estado': 'Caducado'
            },
            2: {
                'Nombre':'Puntualidad',
                'Descripcion':'Premiado/a por no atrasos mensuales',
                'Valor':'50',
                'Fecha vencimiento':'01-04-2024',
                'Estado' : 'Vigente'
            },
        },
        'cargas': {
            1: {
                'nombre': 'Cristian',
                'appaterno': 'Idalgo',
                'apmaterno': 'Contreras',
                'rut': '24824652',
                'dv': 'K',
                'fecha_nacimiento': '05-09-2015',
                'genero': 'Masculino',
                'tipo_carga': 'Simple',
                'tipo_vinculo': 'Hijo(a) directo'
            }
        },
        'documentos': {
        1: {
            "nombre": "curriculum",
            'id': 'YWJjZGVmZ2hpamtsbW5vcA=='
        },
        2:{
            "nombre": "certificado de cargas",
            'id':'YWJjZGVmZ2hasd123assg'
        },
        3:{
            'nombre' : 'antecedentes',
            'id' : 'dHJhaW5lX3N0b3JlMjMz'
        },
        4:{
            'nombre': 'carta de presentacion',
            'id': 'aW50ZXJhY3Rpb25fbWFuYWdlcg==' 
        },
        5:{
            'nombre' : 'organigrama',
            'id' : 'YmFzZTY0X2V4Y2x1c2l2ZQ=='
        },
        },
        'horario': {
            'id_reloj': '681321',
            'nombre_reloj' : '1321-45hrs',
            'ubicacion': 'Entrada principal',
            'fec_inicio': '01-01-2020',
            'fec_termino': '01-01-3000',
            'hora_entrada': '08:00',
            'hora_colacion': '13:00',
            'hora_salida': '17:00',
            'estado': 'Vigente',
        }
    }
}
