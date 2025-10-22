from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria  # <-- ¡AÑADE CATEGORIA AQUÍ!


# Vista para la lista de todos los productos
def lista_productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'catalogo/lista_productos.html', context)


# Vista para el detalle de un solo producto
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    context = {
        'producto': producto
    }
    return render(request, 'catalogo/detalle_producto.html', context)


# --- ¡NUEVA FUNCIÓN! ---
# Vista para los productos filtrados por categoría
def lista_por_categoria(request, categoria_id):
    # Buscamos la categoría por su ID. Si no existe, da un error 404.
    categoria = get_object_or_404(Categoria, id=categoria_id)

    # Filtramos los productos que pertenecen a esa categoría
    productos = Producto.objects.filter(categoria=categoria)

    context = {
        'categoria': categoria,
        'productos': productos
    }
    # Reusaremos la misma plantilla del catálogo principal
    return render(request, 'catalogo/lista_por_categoria.html', context)