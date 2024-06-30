from django.shortcuts import get_object_or_404, redirect, render
from .models import Producto
from .forms import ProductoForm, UserForm
from django.contrib import messages
from django.contrib.auth import logout
from aplicacion.Carrito import Carrito
# Create your views here.
def index(request):
    productos = Producto.objects.all()
    return render(request, 'aplicacion/index.html', {'productos': productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect(to="index")    

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect(to="index")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect(to="index")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect(to="index")




def nosotros(request):
    return render(request,'aplicacion/nosotros.html')

def ubicacion(request):
    return render(request,'aplicacion/ubicacion.html')

def pedidos(request):
    return render(request,'aplicacion/pedidos.html')

def detallecli(request):
    return render(request,'aplicacion/detallecli.html')

def login(request):
    return render(request,'registration/login.html')

def contacto(request):
    return render(request,'aplicacion/contacto.html')

def registrar(request):
    
    form=UserForm()
    
    if request.method=="POST":
        form=UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Se ha Registrado con Exito!")
            return redirect(to="login")
    
    datos={
        "form":form
    }
    return render(request, 'registration/registrar.html',datos)

def salir(request):
    logout(request)
    return redirect(to='index')

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
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        categoria = request.POST.get('categoria')
        imagen = request.FILES.get('imagen')

        # Validaciones simples en el servidor
        if not nombre or not descripcion or not precio or not categoria or not imagen:
            error_message = "Todos los campos son obligatorios"
            datos = {"error_message": error_message}
            return render(request, 'aplicacion/addproduc.html', datos)
        
        # Limpiar y convertir el valor del precio
        try:
            precio = precio.replace('$', '').replace(',', '')
            precio = float(precio)
        except ValueError:
            error_message = "Ingrese un precio válido."
            datos = {"error_message": error_message}
            return render(request, 'aplicacion/addproduc.html', datos)

        # Crear y guardar el nuevo producto
        nuevo_producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            categoria=categoria,
            imagen=imagen
        )
        nuevo_producto.save()
        
        messages.set_level(request,messages.SUCCESS)
        messages.success(request, "Producto creado con exito!!!")
        return redirect('admlista')  # Redirigir a la lista de productos
    
    return render(request, 'aplicacion/addproduc.html')



def ver(request):
    return render(request,'aplicacion/ver.html')



def admlista(request):
    
    admlista=Producto.objects.all()
    
    datos={
        "admlista":admlista
    }
    return render(request,'aplicacion/admlista.html',datos)


def editarprod(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        categoria = request.POST.get('categoria')
        imagen = request.FILES.get('imagen')

        # Validaciones simples en el servidor
        if not nombre or not descripcion or not precio or not categoria:
            error_message = "Todos los campos son obligatorios"
            datos = {"producto": producto, "error_message": error_message}
            return render(request, 'aplicacion/editarprod.html', datos)

        # Limpiar y convertir el valor del precio
        try:
            precio = precio.replace('$', '').replace(',', '')
            precio = float(precio)
        except ValueError:
            error_message = "Ingrese un precio válido."
            datos = {"producto": producto, "error_message": error_message}
            return render(request, 'aplicacion/editarprod.html', datos)

        # Actualizar el producto
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.categoria = categoria
        if imagen:
            producto.imagen = imagen
        producto.save()
        messages.set_level(request,messages.WARNING)
        messages.warning(request,"Producto modificado")
        return redirect('admlista')  # Redirigir a la lista de productos


    imagen_nombre = producto.imagen.name.split('/')[-1] if producto.imagen else None
    datos = {
        "producto": producto,
        "imagen_url": producto.imagen.url if producto.imagen else None,
        "imagen_nombre": imagen_nombre
    }
    return render(request, 'aplicacion/editarprod.html', datos)

def eliminar_producto_2(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        messages.set_level(request,messages.WARNING)
        messages.warning(request,"Producto Eliminado")
    return redirect('admlista')
      

def admusuarios(request):
    return render(request,'aplicacion/admusuarios.html')

def editaruser(request):
    return render(request,'aplicacion/editaruser.html')

def usuarios(request):
    
    return render(request,'registration/usuarios.html')

