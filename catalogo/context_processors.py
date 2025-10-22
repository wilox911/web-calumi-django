from .models import Categoria

def extras_catalogo(request):
    categorias = Categoria.objects.all()
    return {'categorias_menu': categorias}