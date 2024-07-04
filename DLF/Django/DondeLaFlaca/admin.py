from django.contrib import admin
from .models import TipoUsuario,Usuario,TipoProducto,Producto,FormaPago,Pago,Detalle,Despacho

# Register your models here.

admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(FormaPago)
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(Pago)
admin.site.register(Detalle)
admin.site.register(Despacho)