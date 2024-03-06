from django.db import models

# Create your models here.

class Clientes(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()

class Instrumento(models.Model):

    instrumento = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)

class Pedidos(models.Model):

    numPedido = models.IntegerField()
    direccion = models.CharField(max_length=60)

