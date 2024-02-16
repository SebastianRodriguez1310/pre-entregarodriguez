from django.db import models

class Manager(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
   

class TeamLeader(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
   

class Agente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
   

class Area(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    