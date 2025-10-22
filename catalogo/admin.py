from django.contrib import admin
from .models import Categoria, Producto

# Hacemos visibles los modelos en el panel de administración
admin.site.register(Categoria)
admin.site.register(Producto)