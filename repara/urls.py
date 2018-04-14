from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.HomePageView),
	url(r'^clientes/$',views.lista_clientes),
	url(r'^reparaciones/$',views.lista_reparaciones),
	url(r'^equipos/$',views.lista_equipos),
	url(r'^equipo/nuevo/$', views.nuevo_equipo, name='nuevo_equipo'),
	url(r'^equipo/(?P<pk>[0-9]+)/$', views.detalles_equipo, name='detalles_equipo'),
	url(r'^cliente/(?P<pk>[0-9]+)/$', views.detalles_cliente, name='detalles_cliente'),
	url(r'^cliente/(?P<clienteID>[0-9]+)/nuevo_equipo/$', views.nuevo_equipoCliente, name='nuevo_equipoCliente'),
	url(r'^reparacion/(?P<pk>[0-9]+)/$', views.detalles_reparacion, name='detalles_reparacion'),
	url(r'^cliente/nuevo/$', views.nuevo_cliente, name='nuevo_cliente'),
    url(r'^cliente/(?P<pk>[0-9]+)/edit/$', views.editar_cliente, name='editar_cliente'),
    url(r'^cliente/(?P<pk>\d+)/remove/$', views.eliminar_cliente, name='eliminar_cliente'),
    url(r'^empleados/$',views.lista_empleados),
    url(r'^empleado/(?P<pk>[0-9]+)/$', views.detalles_empleado, name='detalles_empleado'),
    url(r'^empleado/nuevo/$', views.nuevo_empleado, name='nuevo_empleado'),
    url(r'^empleado/(?P<pk>[0-9]+)/edit/$', views.editar_empleado, name='editar_empleado'),
    url(r'^empleado/(?P<pk>\d+)/remove/$', views.eliminar_empleado, name='eliminar_empleado'),
    url(r'^reparacion/nuevo/$', views.nueva_reparacion, name='nueva_reparacion'),
    url(r'^reparacion/(?P<pk>[0-9]+)/edit/$', views.editar_reparacion, name='editar_reparacion'),



    

   # url('^cliente/')


]