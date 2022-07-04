from enum import auto
from django.http import HttpResponse
from django.shortcuts import render
from Blog.models import *

def blog(request):
    publicaciones=Publicacion.objects.all
    return render(request, "Blog/blog.html", {"publicaciones": publicaciones})

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    publicaciones=Publicacion.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {'categoria':categoria, 'publicaciones':publicaciones})

