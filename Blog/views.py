from django.http import HttpResponse
from django.shortcuts import render
from Blog.models import *

def blog(request):

    publicaciones=Publicacion.objects.all
    return render(request, "Blog/blog.html", {"publicaciones": publicaciones})


