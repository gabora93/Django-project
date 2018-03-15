from django.urls import path
from repara import views

urlpatterns = [
	path('', views.HomePageView),
	path('clientes/',views.lista_clientes),
	path('reparaciones/',views.lista_reparaciones),
	path('equipos/',views.lista_equipos),
	path('^equipo/nuevo/$', views.nuevo_equipo, name='nuevo_equipo'),
	path('^equipo/(?P<pk>[0-9]+)/$', views.detalles_equipo, name='detalles_equipo'),
	path('^cliente/(?P<pk>[0-9]+)/$', views.detalles_cliente, name='detalles_cliente'),
	path('^cliente/(?P<clienteID>[0-9]+)/nuevo_equipo/$', views.nuevo_equipoCliente, name='nuevo_equipoCliente'),
	path('^reparacion/(?P<pk>[0-9]+)/$', views.detalles_reparacion, name='detalles_reparacion'),
	path('^cliente/nuevo/$', views.nuevo_cliente, name='nuevo_cliente'),
    path('^cliente/(?P<pk>[0-9]+)/edit/$', views.editar_cliente, name='editar_cliente'),
    path('^cliente/(?P<pk>\d+)/remove/$', views.eliminar_cliente, name='eliminar_cliente'),
    path('empleados/',views.lista_empleados),
    path('^empleado/(?P<pk>[0-9]+)/$', views.detalles_empleado, name='detalles_empleado'),
    path('^empleado/nuevo/$', views.nuevo_empleado, name='nuevo_empleado'),
    path('^empleado/(?P<pk>[0-9]+)/edit/$', views.editar_empleado, name='editar_empleado'),
    path('^empleado/(?P<pk>\d+)/remove/$', views.eliminar_empleado, name='eliminar_empleado'),
    path('^reparacion/nuevo/$', views.nueva_reparacion, name='nueva_reparacion'),
    path('^reparacion/(?P<pk>[0-9]+)/edit/$', views.editar_reparacion, name='editar_reparacion'),



    

   # path('^cliente/')


]