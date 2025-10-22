from django.contrib import admin
from django.urls import path, include

# Importaciones para servir archivos de medios en desarrollo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogo.urls')),  # Esto conecta con las URLs de tu app catalogo
]

# Esta línea es la clave para que las imágenes funcionen en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)