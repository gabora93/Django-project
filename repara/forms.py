from django import forms
from .models import Cliente, Equipo, Empleado, Reparacion

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombre','apellido','correo','telefono',)

class EquipoForm(forms.ModelForm):
        
    class Meta:
        model = Equipo
        fields = ('descripcion','modelo',)

class DateInput(forms.DateInput):
    input_type = 'date'



class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'fecha_ingreso': DateInput()
        }

class ReparacionForm(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields = '__all__'
        widgets = {
            'fecha_llegada': DateInput(),
            'fecha_salida': DateInput()
        }
