from django.urls import path
from . import views

urlpatterns = [
    # Ruta de la página principal (la que ya teníamos)
    path('', views.lista_productos, name='lista_productos'),

    # Ruta para el detalle del producto (la que ya teníamos)
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),

    # --- ¡NUEVA RUTA! Para las páginas de categoría ---
    # ej: /categoria/1/ o /categoria/3/
    path('categoria/<int:categoria_id>/', views.lista_por_categoria, name='lista_por_categoria'),
]