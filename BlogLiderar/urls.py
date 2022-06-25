from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('sobre_nosotros', views.sobre_nosotros, name='sobre_nosotros'),
    path('contactapp/', include('ContactApp.urls')),
    path('servicios/', include('Servicios.urls')),
]
