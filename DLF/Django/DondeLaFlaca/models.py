from django.db import models

# Create your models here.
class Tipo_producto(models.Model):
    id_tipo = models.AutoField(primary_key=True, db_column="idTipo")
    descripcion = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return str(self.descripcion)


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, db_column="idProducto")
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()
    id_tipo = models.ForeignKey(
        "Tipo_producto", on_delete=models.CASCADE, db_column="IdTipo"
    )
    imagen = models.ImageField()

    def __str__(self):
        return (
            str(self.id_producto)
            + " "
            + str(self.nombre)
        )