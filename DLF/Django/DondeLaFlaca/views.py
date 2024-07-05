from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import TipoUsuario,Usuario,TipoProducto,Producto,FormaPago,Pago,Detalle,Despacho,Carrito,Item

# Create your views here.
def Principal(request):
    carritos = Carrito.objects.all()
    usuarios = Usuario.objects.all()
    context={
        "usuarios":usuarios,
        "carritos":carritos
    }
    return render(request, 'pages/Principal.html', context)

def Arriendo(request):
    context={}
    return render(request, 'pages/Arriendo.html', context)

def Inicio_sesion(request):
    context={}
    return render(request, 'pages/Inicio_sesion.html', context)

def Mantencion(request):
    context={}
    return render(request, 'pages/Mantencion.html', context)

def Nosotros(request):
    context={}
    return render(request, 'pages/Nosotros.html', context)

def Registro(request):
    context={}
    return render(request, 'pages/Registro.html', context)

def Tienda(request):
    productos = Producto.objects.all()
    context={
        "productos":productos
    }
    return render(request, 'pages/Tienda.html', context)

""" ------------------------------------------------------------------------ """



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
                login(request,user)

                return redirect('Principal')
        else:
            context={
                "message":"Sus contraseñas no coincide",
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
            return render(request,"pages/Principal.html",context)
        else:
            context = {
                "mensaje":"Usuario o contraseña incorrecta",
                "design":"alert alert-danger w-50 mx-auto text-center",
            }
            return render(request,"pages/inicio_sesion.html",context)
    else:
        #Corresponde a redireccionar
        context = {
        }
        return render(request,"pages/inicio_sesion.html",context)

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
    context = {
        "mensaje":"Sesion cerrada",
        "design":"alert alert-info w-50 mx-auto text-center",
    }
    return render(request,"pages/inicio_sesion.html",context)

def pruebafotos(request):
    productos = Producto.objects.all()
    context = {
        "productos":productos
    }
    return render(request,"pages/pruebafotos.html",context)

def addToCart(request,id_prod,cant):
    producto = Producto.objects.get(id_productoq=id_prod)
    if producto.stock >= cant:
        usuario = Usuario.objects.get(user=request.user)
        rut = usuario.rut
        carrito = Carrito.objects.get(rut=rut)
        item = Item(
            id_carrito = carrito,
            id_producto = producto,
            cantidad = cant
        )
        item.save()
        producto.stock = producto.stock - cant
        producto.save()
        
        productos = Producto.objects.all()
        context = {
            "productos":productos
        }

        return render(request,"pages/tienda.html",context)
    else:
        productos = Producto.objects.all()
        context = {
            "message":"stock insuficiente",
            "productos":productos
        }
        return render(request,"pages/tienda.html",context)