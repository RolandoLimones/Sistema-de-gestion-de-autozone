from django.db import models


# Create your models here.
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    proveedor_id = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    almacen_id = models.IntegerField()
    foto = models.URLField()

    def __str__(self):
        return f'Producto: {self.nombre_producto}'