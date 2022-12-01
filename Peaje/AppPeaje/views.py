from django.shortcuts import render, HttpResponseRedirect
from .forms import NuevoTurno,NuevoTicket
from datetime import datetime
from .models import turnos, ticket, operadores
# Create your views here.
from django.http import HttpResponseRedirect
#from Complementos.generar import generarPDF


from .models import tipoVehiculo
from .models import ticket
from .models import estaciones









def index(request):
    context = {'key': 'hola'}
    return render(request, 'AppPeaje/dashboard.html', context=context)

def crearTicket(request):
    return none



def tickets(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NuevoTicket(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            




            vehiculo = form.cleaned_data['tipoVehiculo']

            importe = tipoVehiculo.objects.get(tipo = vehiculo).precio
            #print('importe: {}'.format(importe))

            horario = str(datetime.now())
            fecha = horario.split(' ')[0]
            hora = horario.split(' ')[1].split('.')[0]

            turno_id = list(turnos.objects.all().filter(operador__usuario=request.user , turno_activo = True).values())[0]['id']
            turno = turnos.objects.get(id = turno_id)
            print('turno: {}'.format(turnos.objects.all().filter(operador__usuario=request.user , turno_activo = True).values()))

            #print(turnos.objects.all().values())
            #print(operadores.objects.all().values())

            vehiculo_id = list(tipoVehiculo.objects.all().filter( tipo = vehiculo).values())[-1]['id']
            tipo = tipoVehiculo.objects.get(id = vehiculo_id)
            #print('tipo: {}'.format(tipo))

            tick = ticket(importe=importe, fecha = fecha, hora = hora, tipoVehiculo = tipo, turno = turno)
            print(tick)
            tick.save()
            # ACA VA LA FUNCION
            
            return HttpResponseRedirect('/tickets/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NuevoTicket()
        db = ticket.objects.all()
        print(db)

    activo = len(list(turnos.objects.all().filter(operador__usuario=request.user , turno_activo = True).values())) > 0

    return render(request, 'AppPeaje/tickets.html', {'form': form, 'db':db, 'activo':activo})

def cargar_turnos(request):
    
    if request.method == 'POST':
        
        form = NuevoTurno(request.POST)
        
        if form.is_valid():
            
            fk_operador = operadores.objects.all().filter(usuario=request.user)[0]
            #print(fk_operador)
            #PROCESAR LA INFORMACION
            turno = form.save(commit=False)
            turno.fecha_creacion = datetime.now()
            turno.operador = fk_operador
            turno.save()

            return HttpResponseRedirect('/tickets/')
    else:
        form = NuevoTurno()
    turnos_activos = turnos.objects.all().filter(turno_activo=True, operador__usuario = request.user)

    if len(turnos_activos) > 0:

        activar_form = False

    else:
        activar_form = True        
    return render(request, 'AppPeaje/turnos.html', {'form':form,
                                                    'activar_form':activar_form})


def informe(request):
    #tickets= ticket.objects.all()
    print(' ')
    print(' ')
    print(' ')
    estacions = list(estaciones.objects.values_list('nombre'))


    estacions_dict = {}
    for e in estacions:
        nombre = e[0]
        estacions_dict[nombre] = {}

        importes = ticket.objects.values_list('importe', 'fecha').filter(turno__casilla__estacion__nombre=nombre)
        for im in importes:
            #suma_importes += float(im[0])

            try:
                x = estacions_dict[nombre][str(im[1])]
            except:
                estacions_dict[nombre][str(im[1])] = 0

            estacions_dict[nombre][str(im[1])] += float(im[0])

    print(estacions_dict)
    print(list(estacions_dict))
    print(list(estacions_dict.values()))

    print(ticket.objects.values_list('importe','fecha').filter(turno__casilla__estacion__nombre='ert'))   

    #print(montoEstacion)
    print(' ')
    print(' ')
    print(' ')
    #fecha= ticket.objects.values_list('fecha')
    #for i in fecha:
	    #montoFecha= ticket.objects.values_list('importe').filter(fecha=i)

    return render(request, 'AppPeaje/informe.html', {'estaciones':list(estacions_dict), 'importes':list(estacions_dict.values())})


def terminar_turno(request):
    turnos_activos = turnos.objects.all().filter(turno_activo=True, operador__usuario = request.user)
    try:
        turno = turnos_activos[0]
        turno.turno_activo = False
        turno.fecha_fin = datetime.now()
        turno.save()
    except IndexError:
        pass    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
