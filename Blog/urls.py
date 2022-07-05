from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('buscar/', views.buscar, name="BuscarBlog"),
    path('crearBlog/', views.publicaciones, name='crearBlog'),
    path('mostrar_entradas/', views.mostrar_entradas, name='mostrar_entradas'),
    path('editar_entradas/<int:publicacion_id>', views.editar_entradas, name='editar_entradas'),
    path('eliminar_entradas/<int:publicacion_id>', views.eliminar_entradas, name='eliminar_entradas'),
]


