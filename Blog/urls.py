from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('buscar/', views.buscar, name="BuscarBlog"),
    path('crearBlog/', views.publicaciones, name='crearBlog'),

]


