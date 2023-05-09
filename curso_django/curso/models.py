from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    codigo = models.IntegerField()

