from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import TipoUsuario,Usuario,TipoProducto,Producto,FormaPago,Pago,Detalle,Despacho,Carrito,Item
from .forms import TipoUsuarioForm, UsuarioForm, TipoProductoForm, FormaPagoForm
from django.utils import timezone

# Create your views here.
def Principal(request):
    carritos = Carrito.objects.all()
    usuarios = Usuario.objects.all()
    context={
        "usuarios":usuarios,
        "carritos":carritos
    }
    return render(request, 'pages/Principal.html', context)

def Inicio_sesion(request):
    context={}
    return render(request, 'pages/Inicio_sesion.html', context)

def Nosotros(request):
    context={}
    return render(request, 'pages/Nosotros.html', context)

def Registro(request):
    context={}
    return render(request, 'pages/Registro.html', context)

def VerProducto(request,id_prod):
    producto = Producto.objects.get(id_producto=id_prod)
    tipoProd = producto.id_tipo_producto
    context = {
        "producto":producto,
        "tipoProd":tipoProd
    }
    return render(request, 'pages/Producto.html', context)

def Tienda(request):
    usuarios = Usuario.objects.all()
    tipo = TipoProducto.objects.get(tipo = "Bicicleta")
    productos = Producto.objects.all().filter(id_tipo_producto = tipo)
    carritos = Carrito.objects.all()
    items = Item.objects.all()
    context={
        "usuarios":usuarios,
        "productos":productos,
        "carritos":carritos,
        "items":items
    }
    return render(request, 'pages/Tienda.html', context)

def Tienda_indumentaria(request):
    usuarios = Usuario.objects.all()
    tipo = TipoProducto.objects.get(tipo = "Accesorio")
    tipo2 = TipoProducto.objects.get(tipo = "Pieza")
    productos = Producto.objects.all().filter(Q(id_tipo_producto = tipo)| Q(id_tipo_producto = tipo2))
    carritos = Carrito.objects.all()
    items = Item.objects.all()
    context={
        "usuarios":usuarios,
        "productos":productos,
        "carritos":carritos,
        "items":items
    }
    return render(request, 'pages/Tienda.html', context)
@login_required
def pago_carrito(request):
    formasPago = FormaPago.objects.all()
    usuarios = Usuario.objects.all()
    productos = Producto.objects.all()
    carritos = Carrito.objects.all()
    items = Item.objects.all()
    usuario = Usuario.objects.get(user=request.user)
    carrito = Carrito.objects.get(rut=usuario)
    
    confirm = False
    for i in items:
        if i.id_carrito == carrito:
            confirm = True
            item = i
    context={
        "confirmado":"confirmado",
        "formasPago":formasPago,
        "usuarios":usuarios,
        "productos":productos,
        "carritos":carritos,
        "items":items,
        "confirm":confirm
    }
    return render(request, 'pages/pago_carrito.html', context)
""" ------------------------------------------------------------------------ """
def registrar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        rut = request.POST.get('rut')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        id_tipo_usuario = TipoUsuario.objects.get(tipo='Cliente')

        if confirm == password:
            # Validar y guardar los datos en la base de datos
            if username and rut and first_name and last_name and email and password:
                user = User(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )
                user.set_password(password)
                user.save()

                usuario = Usuario(
                    rut=rut,
                    id_tipo_usuario=id_tipo_usuario,
                    user=user
                )
                usuario.save()

                carrito = Carrito(rut=usuario)
                carrito.save()
                
                login(request,user)
                request.session["tipo"] = usuario.id_tipo_usuario.tipo

                carritos = Carrito.objects.all()
                usuarios = Usuario.objects.all()
                context={
                    "usuarios":usuarios,
                    "carritos":carritos
                }
                return render(request, 'pages/Principal.html', context)
        else:
            context={
                "message":"Sus contraseñas no coinciden",
                "username":username,
                "rut":rut,
                "first_name":first_name,
                "last_name":last_name,
                "email":email,
                "password":password,
                "edit": True
            }
            return render(request,"pages/Registro.html",context)
    else:
        return render(request, 'registro.html')
    
def loginSession(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            request.session["user"] = username
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/despliegue/crud_usuarios.html",context)
        else:
            context ={
                "mensaje":"Usuario o contraseña incorrecta",
                "design" : "alert alert-danger w-50 mx-auto text-center",
            }
            return render(request,"pages/login.html",context)
    else:
        context = {
        }
        return render(request,"pages/login.html",context)

def conectar(request):
    if request.method=="POST":
        #Corresponde al formulario
        username = request.POST["usuario"]
        password = request.POST["pass"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            us = Usuario.objects.get(user=user)
            carrito = Carrito(
                rut = us
            )
            carrito.save()
            request.session["tipo"] = us.id_tipo_usuario.tipo
            carritos = Carrito.objects.all()
            context = {
                "carritos":carritos
            }
            return redirect('Principal')
        else:
            context = {
                "mensaje":"Usuario o contraseña incorrecta"
            }
            return render(request,"pages/inicio_sesion.html",context)
    else:
        #Corresponde a redireccionar
        context = {
        }
        return render(request,"pages/inicio_sesion.html",context)

@login_required
def desconectar(request):
    #del request.session["user"]
    if request.user.is_authenticated:
        user = request.user
        usuario = Usuario.objects.get(user=user)
        rut = usuario.rut
        try:
            carrito = Carrito.objects.get(rut=rut)
            if carrito:
                items = Item.objects.all()
                for tmp in items:
                    if tmp.id_carrito == carrito:
                        tmp.delete()
                carrito.delete()
        except:
            a = 0
        logout(request)
    return redirect('login')
""" ------------------------------------------------------------------------------------ """
def pruebafotos(request):
    productos = Producto.objects.all()
    context = {
        "productos":productos
    }
    return render(request,"pages/pruebafotos.html",context)
""" ------------------------------------------------------------------------------------ """
@login_required
def crud_varios(request):
    tipoUsuarios = TipoUsuario.objects.all()
    formaPago = FormaPago.objects.all()
    tipoProducto = TipoProducto.objects.all()
    context = {
        "tipoUsuarios": tipoUsuarios,
        "formaPago" : formaPago,
        "tipoProducto" : tipoProducto,
    }
    return render(request, "pages/Crud/despliegue/crud_varios.html", context)

@login_required
def crud_productos(request):
    productos = Producto.objects.all()
    tipoProductos = TipoProducto.objects.all()
    context={
        "productos" : productos,
        "tipoProductos" : tipoProductos,
    }
    return render(request, 'pages/Crud/despliegue/crud_productos.html', context)

@login_required
def crud_usuarios(request):
    usuarios = Usuario.objects.all()
    tipoUsuarios = TipoUsuario.objects.all()
    context={
        "usuarios" : usuarios,
        "tipoUsuarios": tipoUsuarios,
    }
    return render(request, 'pages/Crud/despliegue/crud_usuarios.html', context)

@login_required
def crud_ventas(request,pk):
    formapago = FormaPago.objects.all()
    tipoproducto = TipoProducto.objects.all()
    producto = Producto.objects.all()
    usuarios = Usuario.objects.all()
    users = User.objects.all()
    us = Usuario.objects.get(user=request.user)
    rut = us.rut
    pago = Pago.objects.all().filter(rut = rut)

    f = 'filtro'
    c = False
    if pk == 0:
        pago = Pago.objects.all().filter(rut = rut)
    elif pk == 1:
        pago = Pago.objects.all()
        f = 'sin'
        if us.id_tipo_usuario.tipo == 'Cliente':
            c = True
    else:
        pago = Pago.objects.all().filter(rut = rut)
    detalle = Detalle.objects.all()
    despachos = Despacho.objects.all()
    if c:
        context={
            "f":f,
            "usuarios":usuarios,
            "users":users,
            "formapagos":formapago,
            "tipoproductos":tipoproducto,
            "productos":producto,
            "pagos":pago,
            "detalles":detalle,
            "despachos":despachos
        }
    else:
        context={
            "f":f,
            "a":"sssss",
            "usuarios":usuarios,
            "users":users,
            "formapagos":formapago,
            "tipoproductos":tipoproducto,
            "productos":producto,
            "pagos":pago,
            "detalles":detalle,
            "despachos":despachos
        }
    return render(request, 'pages/Crud/despliegue/crud_ventas.html', context)
""" ------------------------------------------------------------------------------------ """
@login_required
def addToCart(request):
    id_prod = request.POST.get('id')
    producto = Producto.objects.get(id_producto=id_prod)
    cant = request.POST.get('cantidad')
    if producto and cant:
        usuario = Usuario.objects.get(user=request.user)
        rut = usuario.rut
        carrito = Carrito.objects.get(rut=rut)
        subtotal = int(producto.precio) * int(cant)
        item = Item(
            id_carrito = carrito,
            id_producto = producto,
            cantidad = cant,
            subtotal = subtotal
        )
        item.save()
        nuevo = producto.stock - int(cant)
        producto.stock = nuevo
        producto.save()
        
        usuarios = Usuario.objects.all()
        tipo = TipoProducto.objects.get(tipo = "Bicicleta")
        productos = Producto.objects.all().filter(id_tipo_producto = tipo)
        carritos = Carrito.objects.all()
        items = Item.objects.all()
        context={
            "usuarios":usuarios,
            "productos":productos,
            "carritos":carritos,
            "items":items
        }

        return render(request,"pages/tienda.html",context)
    else:
        usuarios = Usuario.objects.all()
        tipo = TipoProducto.objects.get(tipo = "Bicicleta")
        productos = Producto.objects.all().filter(id_tipo_producto = tipo)
        carritos = Carrito.objects.all()
        items = Item.objects.all()
        context={
            "usuarios":usuarios,
            "productos":productos,
            "carritos":carritos,
            "items":items
        }
        return render(request,"pages/tienda.html",context)
@login_required
def delToCart(request,pk):
    try:
        item = Item.objects.get(id_item=pk)
        
        cant = item.cantidad
        producto = Producto.objects.get(id_producto = item.id_producto.id_producto)
        nuevo = producto.stock + int(cant)
        producto.stock = nuevo
        producto.save()
        item.delete()

        usuarios = Usuario.objects.all()
        tipo = TipoProducto.objects.get(tipo = "Bicicleta")
        productos = Producto.objects.all().filter(id_tipo_producto = tipo)
        carritos = Carrito.objects.all()
        items = Item.objects.all()
        context={
            "usuarios":usuarios,
            "productos":productos,
            "carritos":carritos,
            "items":items
        }
        return render(request,"pages/tienda.html",context)
    except:
        usuarios = Usuario.objects.all()
        tipo = TipoProducto.objects.get(tipo = "Bicicleta")
        productos = Producto.objects.all().filter(id_tipo_producto = tipo)
        carritos = Carrito.objects.all()
        items = Item.objects.all()
        context={
            "usuarios":usuarios,
            "productos":productos,
            "carritos":carritos,
            "items":items
        }
        return render(request,"pages/tienda.html",context)
@login_required
def pagarCart(request):
    user = request.user
    usuario = Usuario.objects.get(user=user)
    carrito = Carrito.objects.get(rut=usuario)
    items = Item.objects.all().filter(id_carrito = carrito)
    if request.method == 'POST':
        try:
            total = 0
            for tmp in items:
                if tmp.id_carrito == carrito:
                    subtotal = tmp.cantidad * tmp.id_producto.precio
                    total = total + subtotal
            seleccionado = request.POST.get("formaDePago")
            forma = FormaPago.objects.get(id_forma_pago = seleccionado)
            check = request.POST.get("despacho")
            domicilio = False
            if check:
                domicilio = True
            else:
                domicilio = False
            pago = Pago(
                rut = usuario,
                total = total,
                id_forma_pago = forma,
                domicilio = domicilio
            )
            pago.save()
            if check:
                tiempo = timezone.now()
                despa = Despacho(
                    id_pago = pago,
                    pedido = tiempo
                )
                despa.save()
            for tmp in items:
                if tmp.id_carrito == carrito:
                    subtotal = tmp.cantidad * tmp.id_producto.precio
                    producto = tmp.id_producto
                    cantidad = tmp.cantidad
                    detalle = Detalle(
                        id_pago = pago,
                        id_producto = producto,
                        cantidad = cantidad,
                        subtotal = subtotal
                    )
                    detalle.save()
                    tmp.delete()
            carrito.delete()

            carrito = Carrito(
                rut = usuario
            )
            carrito.save()

            usuarios = Usuario.objects.all()
            carritos = Carrito.objects.all()
            items = Item.objects.all()

            formasPago = FormaPago.objects.all()
            productos = Producto.objects.all()
            carritos = Carrito.objects.all()
            items = Item.objects.all()
            usuario = Usuario.objects.get(user=request.user)
            carrito = Carrito.objects.get(rut=usuario)
            
            confirm = False
            for i in items:
                if i.id_carrito == carrito:
                    confirm = True
                    item = i
            context={
                "message":"Compra exitosa...",
                "formasPago":formasPago,
                "usuarios":usuarios,
                "productos":productos,
                "carritos":carritos,
                "items":items,
                "confirm":confirm
            }
            return render(request, 'pages/pago_carrito.html', context)
        except:
            usuarios = Usuario.objects.all()
            tipo = TipoProducto.objects.get(tipo = "Bicicleta")
            productos = Producto.objects.all().filter(id_tipo_producto = tipo)
            carritos = Carrito.objects.all()
            items = Item.objects.all()
            context={
                "usuarios":usuarios,
                "productos":productos,
                "carritos":carritos,
                "items":items
            }
            return render(request,"pages/tienda.html",context)
    else:
        usuarios = Usuario.objects.all()
        tipo = TipoProducto.objects.get(tipo = "Bicicleta")
        productos = Producto.objects.all().filter(id_tipo_producto = tipo)
        carritos = Carrito.objects.all()
        items = Item.objects.all()
        context={
            "usuarios":usuarios,
            "productos":productos,
            "carritos":carritos,
            "items":items
        }
        return render(request,"pages/tienda.html",context)
""" ------------------------------------------------------------------------------------- """
@login_required
def add_tipoUsuario(request):
    form = TipoUsuarioForm()
    if request.method=="POST":
        nuevo = TipoUsuarioForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":form
            }
            return render(request,"pages/Crud/agregar/add_tipoUser.html",context)
    else:
        context = {
            "form":form
        }
        return render(request,"pages/Crud/agregar/add_TipoUser.html",context)
@login_required
def del_tipoUsuario(request, pk):
    try:
        tipoUsuario = TipoUsuario.objects.get(id_tipo_usuario=pk)
        tipoUsuario.delete()

        tipoUsuarios = TipoUsuario.objects.all()
        formaPago = FormaPago.objects.all()
        tipoProducto = TipoProducto.objects.all()
        context = {
            "tipoUsuarios": tipoUsuarios,
            "formaPago" : formaPago,
            "tipoProducto" : tipoProducto,
            "mensaje": "Registro Eliminado",
        }
        return render(request, "pages/Crud/despliegue/crud_varios.html", context)
    except:
        tipoUsuarios = TipoUsuario.objects.all()
        formaPago = FormaPago.objects.all()
        tipoProducto = TipoProducto.objects.all()
        context = {
            "tipoUsuarios": tipoUsuarios,
            "formaPago" : formaPago,
            "tipoProducto" : tipoProducto,
            "mensaje": "Error,Tipo de usuario no encontrado...",
        }
        return render(request, "pages/Crud/despliegue/crud_varios.html", context)
@login_required
def edit_tipoUser(request,pk):
    try:
        tipoUsuarios=TipoUsuario.objects.get(id_tipo_usuario=pk)
        context={}
        if tipoUsuarios:
            print("Se encontró el tipo de usuario")
            if request.method=="POST":
                print("es POST")
                form = TipoUsuarioForm(request.POST, instance=tipoUsuarios)
                form.save()
                mensaje="Se actualizó el tipo de usuario"
                print(mensaje)
                context={'tipoUsuarios':tipoUsuarios, 'form': form, 'mensaje': mensaje}
                return render(request, "pages/Crud/editar/edit_tipoUser.html", context)
            else:
                #no es POST
                print("No es POST")
                form = TipoUsuarioForm(instance=tipoUsuarios)
                mensaje=""
                context={'tipoUsuarios':tipoUsuarios, 'form': form, 'mensaje': mensaje}
                return render(request, "pages/Crud/editar/edit_tipoUser.html", context)
    except:
        print("Error, id no existe")
        tipoUsuarios = TipoUsuario.objects.all()
        mensaje="id no existe"
        context={'mensaje': mensaje, 'tipoUsuarios': tipoUsuarios}
        return render(request, "pages/Crud/despliegue/crud_varios.html", context)

@login_required
def add_forma_pago(request):
    form = FormaPagoForm()
    if request.method=="POST":
        nuevo = FormaPagoForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":form
            }
            return render(request,"pages/Crud/agregar/add_formaPago.html",context)
    else:
        context = {
            "form":form
        }
        return render(request,"pages/Crud/agregar/add_formaPago.html",context)
@login_required
def edit_formaPago(request,pk):

    try:
        formaPago=FormaPago.objects.get(id_forma_pago=pk)
        context={}
        if formaPago:
            print("Se encontró el tipo de usuario")
            if request.method=="POST":
                print("es POST")
                form = FormaPagoForm(request.POST, instance=formaPago)
                form.save()
                mensaje="Se actualizó el tipo de usuario"
                print(mensaje)
                context={'formaPago':formaPago, 'form': form, 'mensaje': mensaje}
                return render(request, "pages/Crud/editar/edit_formaPago.html", context)
            else:
                #no es POST
                print("No es POST")
                form = FormaPagoForm(instance=formaPago	)
                mensaje=""
                context={'tipoProducto':formaPago, 'form': form, 'mensaje': mensaje}
                return render(request, "pages/Crud/editar/edit_formaPago.html", context)
    except:
        print("Error, id no existe")
        formaPago = formaPago.objects.all()
        mensaje="id no existe"
        context={'mensaje': mensaje, 'formaPago': formaPago}
        return render(request, "pages/Crud/despliegue/crud_varios.html", context)
@login_required
def del_formaPago(request, pk):
    try:
        formaPago = FormaPago.objects.get(id_forma_pago=pk)
        formaPago.delete()

        tipoUsuarios = TipoUsuario.objects.all()
        formaPago = FormaPago.objects.all()
        tipoProducto = TipoProducto.objects.all()
        context = {
            "tipoUsuarios": tipoUsuarios,
            "formaPago" : formaPago,
            "tipoProducto" : tipoProducto,
            "mensaje": "Registro Eliminado",
        }
        return render(request, "pages/Crud/despliegue/crud_varios.html", context)
    except:
        tipoUsuarios = TipoUsuario.objects.all()
        formaPago = FormaPago.objects.all()
        tipoProducto = TipoProducto.objects.all()
        context = {
            "tipoUsuarios": tipoUsuarios,
            "formaPago" : formaPago,
            "tipoProducto" : tipoProducto,
            "mensaje": "Error,Tipo de usuario no encontrado...",
        }
        return render(request, "pages/Crud/despliegue/crud_varios.html", context)

@login_required
def add_usuario(request):
    form = UsuarioForm()
    if request.method == "POST":
        nuevo = UsuarioForm(request.POST)
        if nuevo.is_valid():
            usuario_data = nuevo.cleaned_data
            user = User.objects.create_user(
                username=usuario_data["username"],
                password=usuario_data["password"],
            )
            usuario = Usuario(
                user=user,
                rut=usuario_data["rut"],
                id_tipo_usuario=usuario_data["id_tipo_usuario"],
            )
            usuario.save()
            return redirect("crud-usuarios")
    context = {
        "form": form
    }
    return render(request, "pages/Crud/agregar/add_usuario.html", context)
@login_required
def del_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(rut=pk)
        user = User.objects.get(username=usuario.user.username)
        user.delete()
        usuario.delete()

        usuarios = Usuario.objects.all()
        tipoUsuarios = TipoUsuario.objects.all()
        context={
            "mensaje" : "Registro eliminado",
            "usuarios" : usuarios,
            "tipoUsuarios": tipoUsuarios,
        }
        return render(request, 'pages/Crud/despliegue/crud_usuarios.html', context)
    except:
        usuarios = Usuario.objects.all()
        tipoUsuarios = TipoUsuario.objects.all()
        context={
            "usuarios" : usuarios,
            "tipoUsuarios": tipoUsuarios,
        }
        return render(request, 'pages/Crud/despliegue/crud_usuarios.html', context)
@login_required
def edit_usuario(request,pk):

    us = Usuario.objects.get(rut = pk)
    user = User.objects.get(username=us.user.username)

    username = user.username
    rut = us.rut
    first_name = user.first_name
    last_name = user.last_name
    email = user.email
    tipo = us.id_tipo_usuario

    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        id_tipo = request.POST.get("tipousuario")
        id_tipo_usuario = TipoUsuario.objects.get(id_tipo_usuario=id_tipo)

        
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        
        user.save()

        us.id_tipo_usuario=id_tipo_usuario
        
        us.save()
        tipos = TipoUsuario.objects.all()
        context={
            "message":"Actualizado correctamente",
            "tipos":tipos,
            "tipo":tipo,
            "username":username,
            "rut":rut,
            "first_name":first_name,
            "last_name":last_name,
            "email":email
        }
        return render(request,"pages/Crud/editar/edit_usuario.html",context)
    else:
        tipos = TipoUsuario.objects.all()
        context={
            "tipos":tipos,
            "tipo":tipo,
            "username":username,
            "rut":rut,
            "first_name":first_name,
            "last_name":last_name,
            "email":email
        }
        return render(request,"pages/Crud/editar/edit_usuario.html",context)

@login_required
def add_tipo_producto(request):
    form = TipoProductoForm()
    if request.method=="POST":
        nuevo = TipoProductoForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":form
            }
            return render(request,"pages/Crud/agregar/add_tipoProducto.html",context)
    else:
        context = {
            "form":form
        }
        return render(request,"pages/Crud/agregar/add_tipoProducto.html",context)
@login_required
def del_tipoProducto(request, pk):
    try:
        tipoProducto = TipoProducto.objects.get(id_tipo_producto=pk)
        tipoProducto.delete()

        tipoUsuarios = TipoUsuario.objects.all()
        formaPago = FormaPago.objects.all()
        tipoProducto = TipoProducto.objects.all()
        context = {
            "tipoUsuarios": tipoUsuarios,
            "formaPago" : formaPago,
            "tipoProducto" : tipoProducto,
            "mensaje": "Registro Eliminado",
        }
        return render(request, "pages/Crud/despliegue/crud_varios.html", context)
    except:
        tipoUsuarios = TipoUsuario.objects.all()
        formaPago = FormaPago.objects.all()
        tipoProducto = TipoProducto.objects.all()
        context = {
            "tipoUsuarios": tipoUsuarios,
            "formaPago" : formaPago,
            "tipoProducto" : tipoProducto,
            "mensaje": "Error,Tipo de usuario no encontrado...",
        }
        return render(request, "pages/Crud/despliegue/crud_varios.html", context)
@login_required
def edit_tipoProducto(request,pk):

    try:
        tipoProducto=TipoProducto.objects.get(id_tipo_producto=pk)
        context={}
        if tipoProducto:
            print("Se encontró el tipo de usuario")
            if request.method=="POST":
                print("es POST")
                form = TipoProductoForm(request.POST, instance=tipoProducto)
                form.save()
                mensaje="Se actualizó el tipo de usuario"
                print(mensaje)
                context={'tipoProducto':tipoProducto, 'form': form, 'mensaje': mensaje}
                return render(request, "pages/Crud/editar/edit_tipoProducto.html", context)
            else:
                #no es POST
                print("No es POST")
                form = TipoProductoForm(instance=tipoProducto)
                mensaje=""
                context={'tipoProducto':tipoProducto, 'form': form, 'mensaje': mensaje}
                return render(request, "pages/Crud/editar/edit_tipoProducto.html", context)
    except:
        print("Error, id no existe")
        tipoProducto = TipoProducto.objects.all()
        mensaje="id no existe"
        context={'mensaje': mensaje, 'tipoProducto': tipoProducto}
        return render(request, "pages/Crud/despliegue/crud_varios.html", context)
