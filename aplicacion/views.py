from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'aplicacion/index.html')

def nosotros(request):
    return render(request,'aplicacion/nosotros.html')

def ubicacion(request):
    return render(request,'aplicacion/ubicacion.html')

def pedidos(request):
    return render(request,'aplicacion/pedidos.html')

def login(request):
    return render(request,'aplicacion/login.html')

def contacto(request):
    return render(request,'aplicacion/contacto.html')

def registrar(request):
    return render(request,'aplicacion/registrar.html')

def recuperar(request):
    return render(request,'aplicacion/recuperar.html')

def pago(request):
    return render(request,'aplicacion/pago.html')

def admburger(request):
    return render(request,'aplicacion/admburger.html')

def admpedidos(request):
    return render(request,'aplicacion/admpedidos.html')

def admpagregar(request):
    return render(request,'aplicacion/admpagregar.html')

def addproduc(request):
    return render(request,'aplicacion/addproduc.html')

def ver(request):
    return render(request,'aplicacion/ver.html')

def admlista(request):
    return render(request,'aplicacion/admlista.html')

def editarprod(request):
    return render(request,'aplicacion/editarprod.html')

def admusuarios(request):
    return render(request,'aplicacion/admusuarios.html')

def editaruser(request):
    return render(request,'aplicacion/editaruser.html')

def usuarios(request):
    return render(request,'aplicacion/usuarios.html')

