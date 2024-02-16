from django.urls import path
from aplicacion import views

urlpatterns = [
    path('manager/create/', views.manager_create, name='manager_create'),
    path('team_leader/create/', views.team_leader_create, name='team_leader_create'),
    path('agente/create/', views.agente_create, name='agente_create'),
    path('area/create/', views.area_create, name='area_create'),
]
