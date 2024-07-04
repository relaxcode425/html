from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import TipoUsuario,Usuario,TipoProducto,Producto,FormaPago,Pago,Detalle,Despacho

# Create your views here.
def Principal(request):
    context={}
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
    context={}
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
        id_tipo_usuario = TipoUsuario.objects.get(tipo='Cliente')

        # Validar y guardar los datos en la base de datos
        if username and rut and first_name and last_name and email and password and id_tipo_usuario:
            user = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            user.set_password(password)  # Set the password using set_password
            user.save()  # Save the user instance

            usuario = Usuario(
                rut=rut,
                id_tipo_usuario=id_tipo_usuario,
                user=user  # Associate the Usuario with the User
            )
            usuario.save()  # Save the usuario instance
            login(request,user)

            return redirect('Principal')
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
            request.session["tipo"] = us.id_tipo_usuario.tipo
            
            context = {
                
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
        logout(request)
    context = {
        "mensaje":"Sesion cerrada",
        "design":"alert alert-info w-50 mx-auto text-center",
    }
    return render(request,"pages/inicio_sesion.html",context)