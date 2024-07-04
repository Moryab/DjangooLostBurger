from django.shortcuts import get_object_or_404, redirect, render
from .models import Producto, Perfil, Pedido, DatosPago, DetallePedido
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from aplicacion.Carrito import Carrito
from .context_processor import total_carrito

# Create your views here.
def index(request):
    productos = Producto.objects.all()
    return render(request, 'aplicacion/index.html', {'productos': productos})

@login_required
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

@login_required
def pedidos(request):
    pedidos = Pedido.objects.all()
    
    return render(request, 'aplicacion/pedidos.html', {'pedidos': pedidos,})

def detallecli(request, id_pedido):
    pedido = get_object_or_404(Pedido, pk=id_pedido)
    
    # Obtener los detalles del pedido asociados al pedido
    detalles_pedido = DetallePedido.objects.filter(pedido=pedido)
    
    # Calcular el total pagado sumando los subtotales de los detalles
    total_pagado = sum(detalle.subtotal for detalle in detalles_pedido)
    
    context = {
        'pedido': pedido,
        'detalles_pedido': detalles_pedido,
        'total_pagado': total_pagado,
    }
    return render(request, 'aplicacion/detallecli.html', context)

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



@login_required
def pago(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        rut = request.POST.get('rut')
        direccion = request.POST.get('address')
        telefono = request.POST.get('telefono')
        prefijo_telefono = request.POST.get('prefijo')

        # Crear el objeto Pedido
        pedido = Pedido.objects.create(
            cliente=request.user,
            rut=rut,
            direccion=direccion,
            telefono=f"{prefijo_telefono} {telefono}" if prefijo_telefono else telefono,
            total=0.0,  # Ajusta esto según tu lógica de negocio
            estado='Pendiente'  # Ajusta esto según tu lógica de negocio
        )

        # Guardar los productos del carrito como DetallePedido asociados al Pedido
        carrito = Carrito(request)
        for key, item in carrito.carrito.items():
            producto_id = item['producto_id']
            cantidad = item['cantidad']
            precio_unitario = item['acumulado'] / cantidad if cantidad > 0 else 0  # Calcula el precio unitario

            DetallePedido.objects.create(
                pedido=pedido,
                producto_id=producto_id,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                subtotal=item['acumulado']
            )

        # Crear y guardar el objeto DatosPago asociado al Pedido
        datospago = DatosPago.objects.create(
            rut=rut,
            pedido=pedido,
            direccion=direccion,
            telefono=f"{prefijo_telefono} {telefono}" if prefijo_telefono else telefono
        )

        # Limpiar el carrito después de completar el pedido
        carrito.limpiar()

        # Redirigir a una página de confirmación o detalles de pedido
        return redirect('detallecli', id_pedido=pedido.id_pedido)

    # Si es GET o cualquier otro método, simplemente renderiza el formulario vacío
    return render(request, 'aplicacion/pago.html')


def admburger(request):
    return render(request,'aplicacion/admburger.html')

def admpedidos(request):
    if request.method == 'POST':
        id_pedido = request.POST.get('id_pedido')
        nuevo_estado = request.POST.get('estado')
        pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
        if nuevo_estado in [estado[0] for estado in Pedido.ESTADOS_PEDIDO]:
            pedido.estado = nuevo_estado
            pedido.save()
        return redirect('admpedidos')
    
    pedidos = Pedido.objects.all()
    return render(request, 'aplicacion/admpedidos.html', {'pedidos': pedidos})
    

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



def ver(request, id_pedido):
    pedido = get_object_or_404(Pedido, pk=id_pedido)
    
    # Obtener los detalles del pedido asociados al pedido
    detalles_pedido = DetallePedido.objects.filter(pedido=pedido)
    
    # Calcular el total pagado sumando los subtotales de los detalles
    total_pagado = sum(detalle.subtotal for detalle in detalles_pedido)
    
    context = {
        'pedido': pedido,
        'detalles_pedido': detalles_pedido,
        'total_pagado': total_pagado,
    }
    return render(request, 'aplicacion/ver.html', context)



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
    admusuarios = Perfil.objects.all()

    datos = {
        "admusuarios": admusuarios,
    }
    
    return render(request, 'aplicacion/admusuarios.html', datos)

def editaruser(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    perfil = get_object_or_404(Perfil, usuario=usuario)

    if request.method == 'POST':

        usuario.first_name = request.POST.get('nombre')
        usuario.last_name = request.POST.get('apellido')
        usuario.email = request.POST.get('email')
        usuario.is_staff = 'staff' in request.POST
        usuario.is_active = 'is_active' in request.POST

        perfil.telefono = request.POST.get('telefono')
        perfil.prefijo_telefono = request.POST.get('prefijo_telefono')
        perfil.direccion = request.POST.get('direccion')

        usuario.save()
        perfil.save()
        messages.set_level(request,messages.WARNING)
        messages.warning(request,"Usuario modificado")
        return redirect('admusuarios')

    return render(request, 'aplicacion/editaruser.html', {'usuario': usuario, 'perfil': perfil})

def deshabilitar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    usuario.is_active = False
    usuario.save()
    messages.set_level(request,messages.WARNING)
    messages.warning(request,"Usuario Desabilitado!")
    return redirect('admusuarios')  # Redirige a la vista de la lista de usuarios


def usuarios(request):
    
    return render(request,'registration/usuarios.html')

