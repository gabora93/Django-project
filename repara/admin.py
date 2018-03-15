from django.contrib import admin
from .models import Cliente,Reparacion,Equipo,Empleado

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Equipo)
admin.site.register(Reparacion)
admin.site.register(Empleado)
