from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# MODELOS PARA REALIZAR LAS MIGRACIONES PARA CREAR LAS TABLAS EN LA BASE DE DATOS


# MODELO DE CLIENTE
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

# MODELO DE EQUIPO
class Equipo(models.Model):
    cliente = models.ForeignKey('repara.Cliente', related_name='cliente', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    modelo = models.CharField(max_length=30)

# MODELO DE EMPLEADO
class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    estado = models.CharField(max_length=15)
    fecha_ingreso = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# MODELO DE REPARACION
class Reparacion(models.Model):
    empleado = models.ForeignKey('repara.Empleado', related_name='empleado', on_delete=models.CASCADE)
    equipo = models.ForeignKey('repara.Equipo', related_name='equipo', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    fecha_llegada = models.DateField()
    fecha_salida = models.DateField()




