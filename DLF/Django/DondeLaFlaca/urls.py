#from django.conf.urls import url
from django.urls import path
from DondeLaFlaca import views

urlpatterns = [

    path('login', views.conectar, name='login'),
    path('logout', views.desconectar, name='logout'),
    path('registrar', views.registrar, name='registrar'),

    path('', views.Principal, name='Principal'),
    path('arriendo', views.Arriendo, name='arriendo'),
    path('inicio-sesion',views.Inicio_sesion, name='inicio-sesion'),
    path('mantencion',views.Mantencion, name='mantencion'),
    path('nosotros',views.Nosotros, name='nosotros'),
    path('registro',views.Registro, name='registro'),
    path('tienda',views.Tienda, name='tienda'),

    path('addToCart',views.addToCart, name='addToCart'),

    path('pruebafotos',views.pruebafotos, name='pruebafotos'),
]