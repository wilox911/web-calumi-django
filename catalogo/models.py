from django.db import models


# Modelo para las Categorías (Ej: Labiales, Bases, Sombras)
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Modelo para los Productos
class Producto(models.Model):
    # ATRIBUTOS DEL PRODUCTO
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    # RELACIÓN: Un producto pertenece a una categoría.
    # Si se borra una categoría, el campo en el producto se pone nulo (SET_NULL).
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='productos')

    # CAMPO PARA LA IMAGEN (opcional por ahora)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    # MÉTODO PARA QUE SE MUESTRE EL NOMBRE DEL PRODUCTO EN EL ADMIN
    def __str__(self):
        return self.nombre