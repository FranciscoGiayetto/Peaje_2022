from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import NuevoTurno,NuevoTicket
from datetime import datetime
import time

from .models import turnos, ticket, operadores
# Create your views here.
from django.http import HttpResponseRedirect

#from ...Complementos.generar import generarPDF
from .models import tipoVehiculo
from .models import ticket
from .models import estaciones
from .generar import generarPDF, generarPDFTurnos
from .forms import NuevaQueja
from .generar import generarPDF, generarPDFTurnos, generarPDFTicket, generarQR
from .gmail import recibirMailQueja

def quejas(request):
    
    
    if request.method == 'POST':
        
        formito = NuevaQueja(request.POST)
        
        if formito.is_valid():
            
            #PROCESAR LA INFORMACION
            queja = formito.save(commit=False)
            queja.fechaReclamo = datetime.now()
            queja.save()
            queja_dict = {"tituloQueja":queja.tituloQueja,
                          "contenidoQueja":queja.contenidoQueja,
                          "nombreCompleto":queja.nombreCompleto,
                          "gmail": queja.gmail
            }
            recibirMailQueja("ywjrlngnptcvdelw","peajevillada@gmail.com", "peajevillada@gmail.com", queja_dict)
            return HttpResponse("<h3>Queja Validada, espere contestacion en su email en 7 dias habiles</h3>")
    else:
        formito = NuevaQueja()
    
    return render(request, 'AppPeaje/quejas.html', {'formito':formito})




def index(request):
    context = {'key': 'hola'}
    return render(request, 'AppPeaje/dashboard.html', context=context)


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

            casilla=turnos.objects.all().filter(operador__usuario=request.user , turno_activo = True).values()[0]['casilla_id']
            operador=turnos.objects.all().filter(operador__usuario=request.user , turno_activo = True).values()[0]['operador_id']
            DiccTicket={"Numero de ticket ": turno_id, "fecha ": fecha,"hora": hora,"importe": importe, "tipo vehiculo": tipo, "casilla": casilla, "operador": operador}
            generarQR("QR","http://127.0.0.1:8000/tickets/")
            generarPDFTicket(turno_id, DiccTicket.items())
            print(f"Numero de ticket: {turno_id} fecha: {fecha}, hora: {hora}, importe: {importe}, tipo vehiculo: {tipo}, casilla: {casilla}, operador: {operador}")

            tick = ticket(importe=importe, fecha = fecha, hora = hora, tipoVehiculo = tipo, turno = turno)
            print(tick)
            tick.save()
            # ACA VA LA FUNCION
            
            return HttpResponseRedirect('/tickets/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NuevoTicket()
        db = ticket.objects.all().filter(turno__operador__usuario=request.user , turno__turno_activo = True)
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
    fechas = {}
    for e in estacions:
        nombre = e[0]
        estacions_dict[nombre] = {}
        estacions_dict[nombre]['Total'] = 0
        estacions_dict[nombre]['Diario'] = {}

        importes = ticket.objects.values_list('importe', 'fecha').filter(turno__casilla__estacion__nombre=nombre)
        for im in importes:
            fecha = str(im[1])
            fechas[datetime(int(fecha[0:4]), int(fecha[5:7]), int(fecha[8:10])).timestamp()] = fecha

            try:
                x = estacions_dict[nombre]['Diario'][str(im[1])]
            except:
                #172,800 = 2 dias
                #86,400 = 1 dia
                fecha = str(im[1])

                estacions_dict[nombre]['Diario'][str(im[1])] = 0

            estacions_dict[nombre]['Total'] += float(im[0])
            estacions_dict[nombre]['Diario'][str(im[1])] += float(im[0])

    fechas_list = list(fechas)
    fechas_list.sort()
    for est in estacions_dict:
        diarios_keys =  list(estacions_dict[est]['Diario'])
        diarios_values = list(estacions_dict[est]['Diario'].values())
        ind = 0
        for fecha in fechas:
            try:
                estacions_dict[est]['Diario'][fechas[fecha]]
            except:
                diarios_values.insert(ind, 0)
                diarios_keys.insert(ind, fechas[fecha])
                estacions_dict[est]['Diario'][fecha] = 0
            ind += 1

        estacions_dict[est]['Diario'] = {}
        for i in range(len(diarios_keys)):
            estacions_dict[est]['Diario'][diarios_keys[i]] = diarios_values[i]


    print(estacions_dict)
    print(list(estacions_dict))
    print(list(estacions_dict.values()))

    print(ticket.objects.values_list('importe','fecha').filter(turno__casilla__estacion__nombre='ert'))   

    print(' ')
    print(' ')
    print(' ')

    return render(request, 'AppPeaje/informe.html', {'estaciones':estacions_dict})#list(estacions_dict), 'importes':list(estacions_dict.values())})










def terminar_turno(request):
    
    cantidad_emitido = 0
    tickets = list(ticket.objects.all().filter(turno__operador__usuario = request.user, turno__turno_activo = True))
    monto_cobrado = 0
    cantidad_por_categoria = {"Motocicletas":0,
                              "Automoviles":0,
                              "2 ejes":0,
                              "3/4 ejes < 2.10m":0,
                              "3/4 ejes > 2.10m":0,
                              "5/6 ejes":0,
                              "> 6 ejes":0                       
                              }
    
    for i in tickets:
        cantidad_emitido += 1
        monto_cobrado += i.importe
        tipo = i.tipoVehiculo
        print(tipo)
        cantidad_por_categoria[str(tipo)] += 1
        
        
        
        
    print(f"Cantidad de tickets emitidos: {cantidad_emitido} \n monto total cobrado: {monto_cobrado} \n cantidad por categoria: {cantidad_por_categoria}")        
    
    """resultadoQuery = {"cantidadEmitida":cantidad_emitido,
                      "montoCobrado":monto_cobrado,
                      "cantidad_vehiculos_por_categoria":cantidad_por_categoria
                      }"""
    
    date = datetime.now()
    date = date.replace(second=0,microsecond=0)
    generarPDFTurnos(f"turno_informe{date}",cantidad_emitido,monto_cobrado,cantidad_por_categoria.items(),request.user,date)    
    
    
    
    turnos_activos = turnos.objects.all().filter(turno_activo=True, operador__usuario = request.user)
    try:
        turno = turnos_activos[0]
        turno.turno_activo = False
        turno.fecha_fin = datetime.now()
        turno.save()
    except IndexError:
        pass    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




