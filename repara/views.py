from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import TemplateView
from .models import Cliente, Reparacion, Equipo, Empleado
from .forms import ClienteForm, EquipoForm, EmpleadoForm, ReparacionForm

# Create your views here.

def HomePageView(request):
    reparos = [1,2,3]
    return render(request, 'index.html',{'reparos':reparos})
############################
###    REPARACIONES      ###
############################

def lista_reparaciones(request):
    reparaciones = Reparacion.objects.all()
    equipos = Equipo.objects.all()
    return render(request, 'reparaciones.html', {'reparaciones': reparaciones,'equipos':equipos})

def detalles_reparacion(request, pk):
    reparacion = get_object_or_404(Reparacion, pk=pk)
    return render(request, 'detalles_reparacion.html',{'reparacion':reparacion,})

def nueva_reparacion(request):
    title='Nueva Reparación'
    requ=request
    if request.method == "POST":
        form = ReparacionForm(request.POST)
        if form.is_valid():
            reparacion = form.save(commit=False)
            reparacion.user = request.user
            reparacion.save()
            return redirect('detalles_reparacion' ,pk=reparacion.pk)
    else:
        form = ReparacionForm()
    return render(request, 'editar_reparacion.html',{'form':form,'title':title,'requ':requ})



def nuevo_cliente(request):
    title='Nuevo Cliente'
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('detalles_cliente' ,pk=cliente.pk)
    else:
        form = ClienteForm()
    return render(request, 'editar_cliente.html',{'form':form,'title':title})


def editar_reparacion(request, pk):
    title='Editar Reparación'
    reparacion = get_object_or_404(Reparación, pk=pk)
    if request.method == "POST":
        form = ReparacionForm(request.POST, instance=reparacion)
        if form.is_valid():
            reparacion = form.save(commit=False)
            reparacion.save()
            return redirect('detalles_reparacion', pk=reparacion.pk)
    else:
        form = ReparacionForm(instance=reparacion)
    return render(request, 'editar_reparacion.html', {'form': form,'title':title})

############################
###    CLIENTES          ###
############################


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def detalles_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    equipos = Equipo.objects.filter(cliente_id=pk)
    return render(request, 'detalles_cliente.html', {'cliente': cliente,'equipos':equipos})


def editar_cliente(request, pk):
    title='Editar Cliente'
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('detalles_cliente', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'editar_cliente.html', {'form': form,'title':title})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

############################
###    EQUIPOS           ###
############################

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos.html',{'equipos':equipos,})

def nuevo_equipoCliente(request,clienteID):
    cliente = get_object_or_404(Cliente, id=clienteID)
    nombreCompleto = cliente.nombre+' '+cliente.apellido
    title='Añadiendo equipo a: '+ nombreCompleto 
    requ = ''
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.cliente_id = clienteID
            equipo.save()
            requ=request
            return redirect('detalles_equipo' ,pk=equipo.pk)
    else:
        form = EquipoForm()
        requ=request
    return render(request, 'editar_equipo.html',{'form':form,'title':title,'requ':requ})




def nuevo_equipo(request):
    title='Nuevo Equipo'
    requ = ''
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.save()
            requ=request
            return redirect('detalles_equipo' ,pk=equipo.pk)
    else:
        form = EquipoForm()
        requ=request
    return render(request, 'editar_equipo.html',{'form':form,'title':title,'requ':requ})

def detalles_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    clienteID = equipo.cliente_id
    cliente = get_object_or_404(Cliente, id=clienteID)

    return render(request, 'detalles_equipo.html', {'equipo':equipo,'cliente':cliente})


def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados.html', {'empleados': empleados,})

def detalles_empleado(request,pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    return render(request, 'detalles_empleado.html',{'empleado':empleado,})

def nuevo_empleado(request):
    title = 'Nuevo Empleado'
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.save()
            return redirect('detalles_empleado' ,pk=empleado.pk)
    else:
        form = EmpleadoForm()
    return render(request, 'editar_empleado.html',{'form':form,'title':title,})


def editar_empleado(request, pk):
    title='Editar Empleado'
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == "POST":
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.save()
            return redirect('detalles_empleado', pk=empleado.pk)
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'editar_empleado.html', {'form': form,'title':title})


def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    empleado.delete()
    empleados = Empleado.objects.all()
    return render(request, 'empleados.html', {'empleados':empleados}) 

