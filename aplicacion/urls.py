"""
URL configuration for sitio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.urls import path, include
from .views import index, agregar_producto, deshabilitar_usuario, eliminar_producto, restar_producto, limpiar_carrito,  nosotros, ubicacion, pedidos, login, contacto, registrar, recuperar, pago, admburger, admpedidos,admpagregar, ver, addproduc, admlista, editarprod,admusuarios, editaruser, usuarios, detallecli, eliminar_producto_2, salir

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #URLS DE APLICACION
    path('',index,name='index'),
    path('nosotros/',nosotros, name='nosotros'),
    path('ubicacion/',ubicacion, name='ubicacion'),
    path('pedidos/',pedidos, name='pedidos'),
    path('login/',login, name='login'),
    path('contacto/',contacto, name='contacto'),
    path('detallecli/<int:id_pedido>',detallecli, name='detallecli'),
    path('registrar/',registrar, name='registrar'),
    path('recuperar/',recuperar, name='recuperar'),
    path('pago/',pago, name='pago'),
    path('admburger/',admburger, name='admburger'),
    path('admpedidos/',admpedidos, name='admpedidos'),
    path('admpagregar/',admpagregar, name='admpagregar'),
    path('ver/<int:id_pedido>/',ver, name='ver'),
    path('addproduc/',addproduc, name='addproduc'),
    path('admlista/',admlista, name='admlista'),
    path('editarprod/<id>',editarprod, name='editarprod'),
    path('eliminar_producto_2/<id>',eliminar_producto_2, name='eliminar_producto_2'),
    path('admusuarios/',admusuarios, name='admusuarios'),
    path('editaruser/<int:user_id>/',editaruser, name='editaruser'),
    path('usuarios/',usuarios, name='usuarios'),
    path('salir/',salir, name='salir'),
    path('agregar/<int:producto_id>',agregar_producto, name='Add'),
    path('eliminar/<int:producto_id>',eliminar_producto, name='Del'),
    path('restar/<int:producto_id>',restar_producto, name='Sub'),
    path('limpiar/',limpiar_carrito, name='CLS'),
    path('deshabilitar_usuario/<int:user_id>/', deshabilitar_usuario, name='deshabilitar_usuario'),




]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)