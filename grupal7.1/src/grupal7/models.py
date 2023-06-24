from django.db import models

# Create your models here.


class Pedido(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    
class Historial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
