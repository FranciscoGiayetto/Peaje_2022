from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('tickets/', views.tickets, name='tickets'),
    path('turnos/', views.turnos, name='turnos'),
    path('informe/', views.informe, name='informe'),
    path('turnos/', views.cargar_turnos, name='turnos'),
    path('terminar-turno/', views.terminar_turno, name= 'terminar_turno')
]