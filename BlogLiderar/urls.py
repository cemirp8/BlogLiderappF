from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('sobre_nosotros', views.sobre_nosotros, name='sobre_nosotros'),
    path('contactapp/', include('ContactApp.urls')),
    path('servicios/', include('Servicios.urls')),
    path('blog/', include('Blog.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('usuarios/', include('Usuarios.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

handler404 = views.error_404
handler500 = views.error_500