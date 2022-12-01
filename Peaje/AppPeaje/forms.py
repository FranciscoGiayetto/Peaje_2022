from django import forms
from .models import turnos,ticket,quejas



class NuevoTurno(forms.ModelForm):
    class Meta:
        model = turnos
        #fields = '__all__'
        exclude = ('turno_activo', 'fecha_fin','fecha_creacion', 'operador')
        

class NuevoTicket(forms.ModelForm):
    class Meta:
        model = ticket
        #fields = '__all__'
        exclude = ('importe', 'fecha', 'hora', 'turno')

class NuevaQueja(forms.ModelForm):
    class Meta:
        model = quejas
        exclude = ('fechaReclamo',)
        
       