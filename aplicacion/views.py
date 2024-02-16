from django.shortcuts import render
from django.http import HttpResponse
from .forms import ManagerForm, TeamLeaderForm, AgenteForm, AreaForm

def index(request):
    return HttpResponse("¡Bienvenido a la aplicación!")

def manager_create(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("El manager ha sido creado exitosamente.")
    else:
        form = ManagerForm()
    return render(request, 'aplicacion/manager_form.html', {'form': form})

def team_leader_create(request):
    if request.method == 'POST':
        form = TeamLeaderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("El Team Leader ha sido creado exitosamente.")
    else:
        form = TeamLeaderForm()
    return render(request, 'aplicacion/team_leader_form.html', {'form': form})

def agente_create(request):
    if request.method == 'POST':
        form = AgenteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("El Agente ha sido creado exitosamente.")
    else:
        form = AgenteForm()
    return render(request, 'aplicacion/agente_form.html', {'form': form})

def area_create(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("El Area ha sido creado exitosamente.")
    else:
        form = AreaForm()
    return render(request, 'aplicacion/area_form.html', {'form': form})
def inicio(request):
    return HttpResponse("inicio")