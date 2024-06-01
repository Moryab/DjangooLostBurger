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
from .views import index, nosotros, ubicacion, pedidos, login, contacto, registrar, recuperar, pago, admburger, admpedidos,admpagregar, ver, addproduc, admlista, editarprod,admusuarios, editaruser, usuarios

urlpatterns = [
    #URLS DE APLICACION
    path('',index,name='index'),
    path('nosotros/',nosotros, name='nosotros'),
    path('ubicacion/',ubicacion, name='ubicacion'),
    path('pedidos/',pedidos, name='pedidos'),
    path('login/',login, name='login'),
    path('contacto/',contacto, name='contacto'),
    path('registrar/',registrar, name='registrar'),
    path('recuperar/',recuperar, name='recuperar'),
    path('pago/',pago, name='pago'),
    path('admburger/',admburger, name='admburger'),
    path('admpedidos/',admpedidos, name='admpedidos'),
    path('admpagregar/',admpagregar, name='admpagregar'),
    path('ver/',ver, name='ver'),
    path('addproduc/',addproduc, name='addproduc'),
    path('admlista/',admlista, name='admlista'),
    path('editarprod/',editarprod, name='editarprod'),
    path('admusuarios/',admusuarios, name='admusuarios'),
    path('editaruser/',editaruser, name='editaruser'),
    path('usuarios/',usuarios, name='usuarios'),





 





]
