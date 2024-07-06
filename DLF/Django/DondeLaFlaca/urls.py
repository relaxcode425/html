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
    path('ver-producto/<int:id_prod>',views.VerProducto, name='ver-producto'),

    path('crud-productos', views.crud_productos, name='crud-productos'),
    path('crud-usuarios', views.crud_usuarios, name='crud-usuarios'),
    path('crud-varios', views.crud_varios, name='crud-varios'),

    path('addToCart',views.addToCart, name='addToCart'),
    path('pagarCart',views.pagarCart, name='pagarCart'),
    path('delToCart/<str:pk>',views.delToCart, name='delToCart'),

    path('add-tipo-usuario', views.add_tipoUsuario, name='add-tipo-usuario'),
    path('add-usuario', views.add_usuario, name='add-usuario'),
    path('add-forma-pago', views.add_forma_pago, name='add-forma-pago'),
    path('add-tipo-producto', views.add_tipo_producto, name='add-tipo-producto'),

    path('edit-tipo-usuario/<str:pk>', views.edit_tipoUser, name='edit-tipo-usuario'),
    path('edit-tipo-producto/<str:pk>', views.edit_tipoProducto, name='edit-tipo-producto'),
    path('edit-forma-pago/<str:pk>', views.edit_formaPago, name='edit-forma-pago'),

    path('del-tipo-usuario/<str:pk>', views.del_tipoUsuario, name='del-tipo-usuario'),
    path('del-tipo-producto/<str:pk>', views.del_tipoProducto, name='del-tipo-producto'),
    path('del-forma-pago/<str:pk>', views.del_formaPago, name='del-forma-pago'),

    path('pruebafotos',views.pruebafotos, name='pruebafotos'),
]