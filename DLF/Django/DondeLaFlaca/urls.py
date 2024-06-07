#from django.conf.urls import url
from django.urls import path
from DondeLaFlaca import views

urlpatterns = [
    path('', views.Principal, name='Principal'),
    path('arriendo', views.Arriendo, name='arriendo'),
    path('inicio-sesion',views.Inicio_sesion, name='inicio-sesion'),
    path('mantencion',views.Mantencion, name='mantencion'),
    path('nosotros',views.Nosotros, name='nosotros'),
    path('registro',views.Registro, name='registro'),
    path('tienda',views.Tienda, name='tienda'),
]