from django.shortcuts import render

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