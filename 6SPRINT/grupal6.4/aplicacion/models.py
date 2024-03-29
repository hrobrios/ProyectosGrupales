from django.db import models
import datetime

# Create your models here.
class Club(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField(verbose_name="Mail del jugador", unique=True)
    celular = models.CharField(max_length=15, null=True)
    telefono = models.CharField(max_length=15, default="")
    egreso = models.IntegerField(default=2009)
    fecha_contratacion = models.DateField(datetime.date.today())

    def __str__(self):
        return self.apellido
    
class Entrenador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField(verbose_name="", unique=True)
    celular = models.CharField(max_length=15, null=True)
    telefono = models.CharField(max_length=15, default="")
    egreso = models.IntegerField()
    fecha_contratacion = models.DateField(datetime.date.today())


    def __str__(self):
        return self.apellido