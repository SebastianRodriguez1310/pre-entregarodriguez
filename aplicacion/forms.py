from django import forms
from .models import Manager, TeamLeader, Agente, Area

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['nombre', 'edad', 'salario']

class TeamLeaderForm(forms.ModelForm):
    class Meta:
        model = TeamLeader
        fields = ['nombre', 'departamento', 'fecha_contratacion']

class AgenteForm(forms.ModelForm):
    class Meta:
        model = Agente
        fields = ['nombre', 'telefono', 'correo']

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nombre', 'descripcion']